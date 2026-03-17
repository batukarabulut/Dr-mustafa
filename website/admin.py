from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteImage,
    SiteSettings,
    ContactSubmission,
    TranslatableContent,
    HomeContent,
    AboutContent,
    ContactContent,
    FransizAskisiContent,
    RinoplastiContent,
    DolguContent,
    BotoksContent,
    MezoterapiContent,
    PrpContent,
    MemeEstetigiContent,
    YuzEstetigiContent,
    VucutEstetigiContent,
    JinekomastiContent,
)


# ----- Site görselleri (admin'den yüklenebilir) -----
@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ("key", "label", "page_group", "image_type", "image_preview", "has_image")
    list_editable = ("label",)
    list_filter = ("key",)
    list_display_links = ("key",)
    search_fields = ("key", "label")
    ordering = ("key",)
    fieldsets = (
        (None, {"fields": ("key", "label")}),
        (
            "Görsel",
            {
                "fields": ("image",),
                "description": "Görsel yükleyin. Yüklemezseniz statik varsayılan kullanılır. Kaydettikten sonra sayfa yenilendiğinde yeni görsel görünecektir.",
            },
        ),
    )

    # Sayfa adı eşleme
    PAGE_GROUPS = {
        "logo": "Genel",
        "mainpage": "Anasayfa",
        "about": "Hakkımda",
        "botoks": "Botoks",
        "rinoplasti": "Rinoplasti",
        "dolgu": "Dolgu",
        "mezoterapi": "Mezoterapi",
        "prp": "PRP",
        "fransiz_askisi": "Fransız Askısı",
        "meme_estetigi": "Meme Estetiği",
        "yuz_estetigi": "Yüz Estetiği",
        "vucut_estetigi": "Vücut Estetiği",
        "jinekomasti": "Jinekomasti",
    }

    def page_group(self, obj):
        """Görselin ait olduğu sayfa."""
        for prefix, name in self.PAGE_GROUPS.items():
            if obj.key.startswith(prefix):
                return name
        return "Diğer"

    page_group.short_description = "Sayfa"

    def image_type(self, obj):
        """Görsel türü (hero veya card)."""
        if obj.key.endswith("_hero"):
            return "Hero"
        elif obj.key.endswith("_card"):
            return "Bilgi Kartı"
        return "Genel"

    image_type.short_description = "Tür"

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 100px; object-fit: contain; border-radius: 4px;">', obj.image.url)
        return "—"

    image_preview.short_description = "Önizleme"

    def has_image(self, obj):
        return "✓" if obj and obj.image else "—"

    has_image.short_description = "Yüklü"

    def changelist_view(self, request, extra_context=None):
        """Sayfa yüklendiğinde eksik görsel kayıtlarını otomatik oluştur."""
        from .image_utils import ensure_image_entries
        ensure_image_entries()
        return super().changelist_view(request, extra_context=extra_context)


# ----- Genel bilgiler (tek kayıt) -----
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("doctor_name", "phone", "email")
    fieldsets = (
        ("Kişi / İletişim", {"fields": ("doctor_name", "phone", "whatsapp", "email", "address")}),
        ("Sosyal medya", {"fields": ("instagram_url", "facebook_url")}),
        ("Footer", {"fields": ("footer_copyright", "developer_credit")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ----- İletişim formu gönderileri -----
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "created_at", "source")
    list_filter = ("source", "created_at")
    search_fields = ("name", "email", "phone", "message", "subject")
    readonly_fields = ("name", "email", "phone", "subject", "message", "kvkk", "created_at", "source")
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False


# ----- Sayfa içerikleri: ortak admin (slug prefix filtresi) -----
def make_page_content_admin(prefix, short_name):
    """prefix: örn. 'home_', short_name: 'home' (yeni kayıt eklerken slug ön eki)."""

    class PageContentAdmin(admin.ModelAdmin):
        list_display = ("slug", "label", "has_tr", "has_en", "has_de", "preview_tr")
        search_fields = ("slug", "label", "content_tr", "content_en", "content_de")
        fieldsets = (
            (None, {"fields": ("slug", "label")}),
            ("Türkçe", {"fields": ("content_tr",)}),
            ("İngilizce (EN)", {"fields": ("content_en",)}),
            ("Almanca (DE)", {"fields": ("content_de",)}),
        )

        def get_queryset(self, request):
            qs = super().get_queryset(request)
            return qs.filter(slug__startswith=prefix)

        def save_model(self, request, obj, form, change):
            if obj.slug and not obj.slug.startswith(prefix):
                obj.slug = prefix + obj.slug.lstrip("_")
            super().save_model(request, obj, form, change)

        def has_tr(self, obj):
            return "✓" if (obj.content_tr or "").strip() else "—"

        has_tr.short_description = "TR"

        def has_en(self, obj):
            return "✓" if (obj.content_en or "").strip() else "—"

        has_en.short_description = "EN"

        def has_de(self, obj):
            return "✓" if (obj.content_de or "").strip() else "—"

        has_de.short_description = "DE"

        def preview_tr(self, obj):
            text = (obj.content_tr or "")[:50]
            if len(obj.content_tr or "") > 50:
                text += "…"
            return text

        preview_tr.short_description = "Önizleme"

    return PageContentAdmin


# Her sayfa için ayrı admin bölümü (menüde ayrı görünür)
admin.site.register(HomeContent, make_page_content_admin("home_", "home"))
admin.site.register(AboutContent, make_page_content_admin("about_", "about"))
admin.site.register(ContactContent, make_page_content_admin("contact_", "contact"))
admin.site.register(FransizAskisiContent, make_page_content_admin("fransiz_askisi_", "fransiz_askisi"))
admin.site.register(RinoplastiContent, make_page_content_admin("rinoplasti_", "rinoplasti"))
admin.site.register(DolguContent, make_page_content_admin("dolgu_", "dolgu"))
admin.site.register(BotoksContent, make_page_content_admin("botoks_", "botoks"))
admin.site.register(MezoterapiContent, make_page_content_admin("mezoterapi_", "mezoterapi"))
admin.site.register(PrpContent, make_page_content_admin("prp_", "prp"))
admin.site.register(MemeEstetigiContent, make_page_content_admin("meme_estetigi_", "meme_estetigi"))
admin.site.register(YuzEstetigiContent, make_page_content_admin("yuz_estetigi_", "yuz_estetigi"))
admin.site.register(VucutEstetigiContent, make_page_content_admin("vucut_estetigi_", "vucut_estetigi"))
admin.site.register(JinekomastiContent, make_page_content_admin("jinekomasti_", "jinekomasti"))
