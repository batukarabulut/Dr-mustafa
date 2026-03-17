from django.db import models


class SiteImage(models.Model):
    """
    Sitede kullanılan görseller. Admin'den yüklenebilir; yoksa statik varsayılan kullanılır.
    key: benzersiz anahtar (örn. logo, mainpage1, dolgu_card)
    """
    key = models.SlugField(max_length=80, unique=True, verbose_name="Anahtar")
    image = models.ImageField(
        upload_to="site_images/%Y/%m/",
        blank=True,
        null=True,
        verbose_name="Görsel",
        help_text="Yüklemezseniz statik varsayılan görsel kullanılır.",
    )
    label = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Açıklama (admin)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Son güncelleme",
        help_text="Görsel değiştiğinde cache busting için kullanılır.",
    )

    class Meta:
        verbose_name = "Site görseli"
        verbose_name_plural = "Site görselleri"
        ordering = ["key"]

    def __str__(self):
        return self.label or self.key


class SiteSettings(models.Model):
    """
    Sitelerin genel bilgileri – tek kayıt (singleton). Admin'de "Genel Bilgiler" ile düzenlenir.
    """
    doctor_name = models.CharField(max_length=200, default="Op. Dr. Mustafa Öksüz", verbose_name="Doktor adı")
    phone = models.CharField(max_length=30, default="+90 540 740 40 77", verbose_name="Telefon")
    whatsapp = models.CharField(max_length=30, default="905407404077", verbose_name="WhatsApp (ülke kodu ile, başında + yok)")
    email = models.EmailField(blank=True, verbose_name="E-posta")
    address = models.TextField(blank=True, verbose_name="Adres")
    footer_copyright = models.CharField(
        max_length=200,
        default="Tüm hakları saklıdır.",
        verbose_name="Footer telif metni",
    )
    instagram_url = models.URLField(blank=True, default="https://www.instagram.com/plasticsurgeon.mustafaoksuz/", verbose_name="Instagram URL")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    developer_credit = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Geliştirici notu (footer)",
        help_text="Örn: Bu site X tarafından geliştirilmiştir.",
    )

    class Meta:
        verbose_name = "Genel bilgiler"
        verbose_name_plural = "Genel bilgiler"

    def __str__(self):
        return self.doctor_name

    @classmethod
    def get_singleton(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={"doctor_name": "Op. Dr. Mustafa Öksüz"})
        return obj


class ContactSubmission(models.Model):
    """İletişim / randevu formu gönderileri – admin'den görüntülenir."""
    name = models.CharField(max_length=200, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    subject = models.CharField(max_length=200, blank=True, verbose_name="Konu")
    message = models.TextField(verbose_name="Mesaj")
    kvkk = models.BooleanField(default=True, verbose_name="KVKK onayı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim tarihi")
    source = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Kaynak",
        help_text="Örn. contact, home, api",
    )

    class Meta:
        verbose_name = "İletişim formu gönderisi"
        verbose_name_plural = "İletişim formu gönderileri"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} – {self.created_at.strftime('%d.%m.%Y %H:%M')}"


class TranslatableContent(models.Model):
    """
    Site veya sayfa metinleri: Admin'den TR/EN/DE için düzenlenebilir.
    slug: benzersiz anahtar (örn. fransiz_askisi_hero_title)
    """
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Anahtar")
    label = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Açıklama (admin)",
        help_text="Admin listesinde görünsün diye kısa açıklama",
    )
    content_tr = models.TextField(blank=True, verbose_name="İçerik (Türkçe)")
    content_en = models.TextField(blank=True, verbose_name="İçerik (İngilizce)")
    content_de = models.TextField(blank=True, verbose_name="İçerik (Almanca)")

    class Meta:
        verbose_name = "Çevrilebilir içerik"
        verbose_name_plural = "Çevrilebilir içerikler"
        ordering = ["slug"]

    def __str__(self):
        return self.label or self.slug

    def get_for_language(self, language_code):
        """Örn. 'tr', 'en', 'de' için doğru alanı döndürür. Yoksa TR fallback."""
        lang = (language_code or "tr")[:2].lower()
        if lang == "tr":
            return self.content_tr or ""
        if lang == "de":
            return self.content_de or self.content_tr or ""
        return self.content_en or self.content_tr or ""


# Proxy modeller: Admin'de her sayfa ayrı menü olarak görünsün
class HomeContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Anasayfa içeriği"
        verbose_name_plural = "Anasayfa içerikleri"


class AboutContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Hakkımızda içeriği"
        verbose_name_plural = "Hakkımızda içerikleri"


class ContactContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "İletişim içeriği"
        verbose_name_plural = "İletişim içerikleri"


class FransizAskisiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Fransız Askısı içeriği"
        verbose_name_plural = "Fransız Askısı içerikleri"


class RinoplastiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Rinoplasti içeriği"
        verbose_name_plural = "Rinoplasti içerikleri"


class DolguContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Dolgu içeriği"
        verbose_name_plural = "Dolgu içerikleri"


class BotoksContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Botoks içeriği"
        verbose_name_plural = "Botoks içerikleri"


class MezoterapiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Mezoterapi içeriği"
        verbose_name_plural = "Mezoterapi içerikleri"


class PrpContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "PRP içeriği"
        verbose_name_plural = "PRP içerikleri"


class MemeEstetigiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Meme Estetiği içeriği"
        verbose_name_plural = "Meme Estetiği içerikleri"


class YuzEstetigiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Yüz Estetiği içeriği"
        verbose_name_plural = "Yüz Estetiği içerikleri"


class VucutEstetigiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Vücut Estetiği içeriği"
        verbose_name_plural = "Vücut Estetiği içerikleri"


class JinekomastiContent(TranslatableContent):
    class Meta:
        proxy = True
        verbose_name = "Jinekomasti içeriği"
        verbose_name_plural = "Jinekomasti içerikleri"
