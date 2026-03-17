from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, label=_("Ad Soyad"))
    email = forms.EmailField(label=_("E-posta"))
    phone = forms.CharField(max_length=50, label=_("Telefon"))
    subject = forms.CharField(max_length=200, required=False, label=_("Konu"))
    message = forms.CharField(widget=forms.Textarea, label=_("Mesajınız"))
    kvkk = forms.BooleanField(label=_("KVKK onayı"), required=True)

