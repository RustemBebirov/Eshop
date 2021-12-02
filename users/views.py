from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, authenticate, login as django_login , logout as django_logout
from django.contrib import messages
from django.urls import reverse_lazy 
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.utils.encoding import force_text 
from users.tasks import send_confirmation_mail 
from users.tools.token import account_activation_token 
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required


User = get_user_model()

@login_required(login_url="{% url 'login' %}")
def user_profile(request):
    form = UserProfileForm(instance=request.user)
    if request.method == 'POST':
            form = UserProfileForm(request.POST,request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('profile'))

    context = {
        'form':form
    }
    return render(request,'user_profile.html',context)


def logout(request):
    django_logout(request)
    messages.success(request,'You logged out')
    return redirect(reverse_lazy('home:index'))


def login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email,password=password)
        if user:
            django_login(request,user)
            messages.success(request,'You logged in successfuly')
            return redirect(reverse_lazy('home:index'))
        else:
            messages.error(request,'The information you entered is valid')

    context = {
        'form':form
    }
    return render(request,'login.html',context)  

def register(request): 
    form = RegistrationForm() 
    if request.method == 'POST': 
        form = RegistrationForm(data=request.POST) 
        if form.is_valid(): 
            user = form.save(commit=False) 
            user.is_active = False 
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST'] 
            send_confirmation_mail(user_id=user.id, site_address=site_address) 
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('home:index'))
    context = {
    'form': form,
    }
    return render(request, 'register.html', context)

def activate(request, uidb64, token): 

    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except:
        (TypeError, ValueError, OverflowError, User.DoesNotExist) 
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:index'))

    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('register'))

    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('register'))