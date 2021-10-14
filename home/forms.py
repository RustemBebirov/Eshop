from django.forms import ModelForm, TextInput,Textarea
from .models import ContactUs

class ContactForm(ModelForm):
    class Meta:

        model = ContactUs
        fields = ['name','email','subject','phone','message']
        widgets = {
            'name' : TextInput(attrs={'placeholder':'Your Name'}),
            'subject' : TextInput(attrs={'placeholder':'Subject'}),
            'email' : TextInput(attrs={'placeholder':'Email Address'}),
            'phone' : TextInput(attrs={'placeholder':'Your Phone'}),
            'message' : Textarea(attrs={'placeholder':'Your Message'}),

        }

        def send_email(self):
            # send email using the self.cleaned_data dictionary
            pass