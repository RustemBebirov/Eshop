from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfile(forms.ModelForm):
    model = User
    fields = ("phone",'country','city','address','image')



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=127,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    password = forms.CharField(max_length=127,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))

class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'})
    )
   
    password2 = forms.CharField(label='Confirm',widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}),
    
    
    )

    agree = forms.BooleanField(label="""I agree all statements in  <a href="/pages/privacy" class='term-service'>Terms of service</a>""",
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            
        )