
from product.models import Category, Product
from django.shortcuts import render
from .models import Settings
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse


def index(request):
    # settings = Settings.objects.get(id=1)
    products = Product.objects.all()
    category = Category.objects.all()
    context= {
        # 'settings':settings,
        'page':'home',
        'category':category,
        'products':products,
        
    }
    return render(request,'index.html',context)

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'form submission success..')
        return reverse('home:index')

    def form_valid(self, form):
        contact=form.save()
        contact.ip = self.request.META.get('REMOTE_ADDR')
        contact.save()
        return super().form_valid(form)
