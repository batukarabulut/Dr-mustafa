from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    name = models.CharField('Ad Soyad', max_length=35)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=16)
    subject = models.CharField('Konu', max_length=200)
    message = models.TextField('Mesaj', max_length=500)

    #default fields
    created_at = models.DateTimeField('Gönderilme Tarihi', auto_now_add=True)
    is_read = models.BooleanField('Okundu mu?', default=False)

    class Meta:
        verbose_name = 'İletişim Formu'
        verbose_name_plural = 'İletişim Formları'
        ordering = ['-created_at'] #show newest

    def __str__(self):
        return f"{self.name} - {self.subject}"
