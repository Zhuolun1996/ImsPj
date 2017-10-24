from django import forms
from captcha.fields import CaptchaField
from .models import ask


class askForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ask
        fields = '__all__'
