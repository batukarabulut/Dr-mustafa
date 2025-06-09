from django.db import models
from django.utils import timezone

class contactSubmission(models.Model):
    name = models.CharField('Ad Soyad', max_length=35)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=16)
    subject = models.CharField('Konu', max_length=200)
    message = models.textField('Mesaj')
