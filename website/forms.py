from django import forms
from website.models import contact , newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
class contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'

class newsletterform(forms.ModelForm):

    
    class Meta:
        model = newsletter
        fields = '__all__'
