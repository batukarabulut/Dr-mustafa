"""
Site görselleri: Admin'den yüklenen veya statik varsayılan.
"""
from django.conf import settings

from .models import SiteImage

# Anahtar -> (statik dosya yolu, admin açıklaması)
# Her hizmet sayfası için xxx_hero (hero section) ve xxx_card (bilgi kartı) standart yapıdadır.
IMAGE_DEFAULTS = {
    # ── Genel ──
    "logo":                   ("assets/images/logo.png",                     "Site Logosu"),
    "mainpage1":              ("assets/images/hero-aesthetic.jpg",              "Anasayfa – Hero Görseli 1"),
    "mainpage2":              ("assets/images/mainpage2.webp",               "Anasayfa – Hero Görseli 2"),
    "about_hero":             ("assets/images/hero-aesthetic.jpg",              "Hakkımda – Ana Görsel"),
    "about_card":             ("assets/images/hero-aesthetic.jpg",             "Hakkımda – Bilgi Kartı (Anasayfa)"),

    # ── Anasayfa Slider Görselleri ──
    "hero_slide_1":           ("assets/images/hero-aesthetic.jpg",            "Anasayfa Slider – Slide 1 (Genel)"),
    "hero_slide_2":           ("assets/images/rinoplasti.png",               "Anasayfa Slider – Slide 2 (Rinoplasti)"),
    "hero_slide_3":           ("assets/images/meme-estetigi-card.jpg",       "Anasayfa Slider – Slide 3 (Meme Estetiği)"),
    "hero_slide_4":           ("assets/images/botoks-card.jpg",              "Anasayfa Slider – Slide 4 (Botoks)"),

    # ── Botoks ──
    "botoks_hero":            ("assets/images/botoks-card.jpg",              "Botoks – Hero Görseli"),
    "botoks_card":            ("assets/images/botoks-card.jpg",              "Botoks – Bilgi Kartı Görseli"),

    # ── Rinoplasti ──
    "rinoplasti_hero":        ("assets/images/rinoplasti.png",               "Rinoplasti – Hero Görseli"),
    "rinoplasti_card":        ("assets/images/rinoplasti.png",               "Rinoplasti – Bilgi Kartı Görseli"),

    # ── Dolgu ──
    "dolgu_hero":             ("assets/images/dolgu-card.jpg",               "Dolgu – Hero Görseli"),
    "dolgu_card":             ("assets/images/dolgu-card.jpg",               "Dolgu – Bilgi Kartı Görseli"),

    # ── Mezoterapi ──
    "mezoterapi_hero":        ("assets/images/dolgu-card.jpg",               "Mezoterapi – Hero Görseli"),
    "mezoterapi_card":        ("assets/images/dolgu-card.jpg",               "Mezoterapi – Bilgi Kartı Görseli"),

    # ── PRP ──
    "prp_hero":               ("assets/images/pexels-cottonbro-7585311.jpg", "PRP – Hero Görseli"),
    "prp_card":               ("assets/images/pexels-cottonbro-7585311.jpg", "PRP – Bilgi Kartı Görseli"),

    # ── Fransız Askısı ──
    "fransiz_askisi_hero":    ("assets/images/pexels-cottonbro-7585311.jpg", "Fransız Askısı – Hero Görseli"),
    "fransiz_askisi_card":    ("assets/images/pexels-cottonbro-7585311.jpg", "Fransız Askısı – Bilgi Kartı Görseli"),

    # ── Meme Estetiği ──
    "meme_estetigi_hero":     ("assets/images/meme-estetigi-card.jpg",       "Meme Estetiği – Hero Görseli"),
    "meme_estetigi_card":     ("assets/images/meme-estetigi-card.jpg",       "Meme Estetiği – Bilgi Kartı Görseli"),

    # ── Yüz Estetiği ──
    "yuz_estetigi_hero":      ("assets/images/yuz-estetigi-card.jpg",        "Yüz Estetiği – Hero Görseli"),
    "yuz_estetigi_card":      ("assets/images/yuz-estetigi-card.jpg",        "Yüz Estetiği – Bilgi Kartı Görseli"),

    # ── Vücut Estetiği ──
    "vucut_estetigi_hero":    ("assets/images/vucut-estetigi-card.jpg",      "Vücut Estetiği – Hero Görseli"),
    "vucut_estetigi_card":    ("assets/images/vucut-estetigi-card.jpg",      "Vücut Estetiği – Bilgi Kartı Görseli"),

    # ── Jinekomasti ──
    "jinekomasti_hero":       ("assets/images/vucut-estetigi-card.jpg",      "Jinekomasti – Hero Görseli"),
    "jinekomasti_card":       ("assets/images/vucut-estetigi-card.jpg",      "Jinekomasti – Bilgi Kartı Görseli"),
}


def get_site_images(request=None):
    """
    Her anahtar için URL döndürür: Admin'de yüklü görsel varsa onun URL'i,
    yoksa statik varsayılan. Şablonda site_images.logo, site_images.botoks_hero vb. kullanılır.
    """
    result = {}
    static_prefix = "/" + (settings.STATIC_URL or "static/").strip("/")
    if not static_prefix.endswith("/"):
        static_prefix += "/"

    keys = set(IMAGE_DEFAULTS.keys())
    db_images = {obj.key: obj for obj in SiteImage.objects.filter(key__in=keys) if obj.image}
    for key, (default_path, _label) in IMAGE_DEFAULTS.items():
        if key in db_images:
            url = db_images[key].image.url
            # Cache busting: görsel güncellendiğinde tarayıcı yeni dosyayı çeksin
            ts = getattr(db_images[key], "updated_at", None)
            if ts:
                sep = "&" if "?" in url else "?"
                url = f"{url}{sep}v={int(ts.timestamp())}"
            # Tam URL (proxy/CDN için)
            if request and hasattr(request, "build_absolute_uri"):
                url = request.build_absolute_uri(url)
            result[key] = url
        else:
            url = static_prefix + default_path.lstrip("/")
            if request and hasattr(request, "build_absolute_uri"):
                url = request.build_absolute_uri(url)
            result[key] = url
    return result


def ensure_image_entries():
    """
    IMAGE_DEFAULTS'taki tüm anahtarların veritabanında SiteImage kaydı olmasını sağlar.
    Eksik olanları varsayılan açıklamalarıyla oluşturur.
    Admin ilk açıldığında veya migration sonrası çağrılabilir.
    """
    existing_keys = set(SiteImage.objects.values_list("key", flat=True))
    new_entries = []
    for key, (_path, label) in IMAGE_DEFAULTS.items():
        if key not in existing_keys:
            new_entries.append(SiteImage(key=key, label=label))
    if new_entries:
        SiteImage.objects.bulk_create(new_entries, ignore_conflicts=True)
    return len(new_entries)
