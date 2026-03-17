"""
Dil geçişi için aynı sayfanın hedef dil URL'lerini context'e ekler.
Genel site bilgileri (SiteSettings) tüm şablonlara eklenir.
"""
from django.conf import settings

from .models import SiteSettings


def path_for_language(path, lang_code):
    """Mevcut path için hedef dil URL'ini döndürür. Örn: /tr/contact/ + en -> /en/contact/"""
    if not path or not path.startswith("/"):
        return f"/{lang_code}/"
    has_trailing_slash = path.endswith("/") and path != "/"
    path = path.rstrip("/") or "/"
    parts = path.split("/")
    lang_codes = dict(settings.LANGUAGES)
    if len(parts) >= 2 and parts[1] in lang_codes:
        rest = "/".join(parts[2:])
        tail = f"/{rest}/" if rest else "/"
        return f"/{lang_code}{tail}" if rest else f"/{lang_code}/"
    rest = path.lstrip("/")
    tail = f"/{rest}/" if rest and has_trailing_slash else (f"/{rest}" if rest else "")
    return f"/{lang_code}{tail}" if tail else f"/{lang_code}/"


def language_switch_urls(request):
    """Şablonda next_tr, next_en, next_de olarak kullanılır."""
    path = getattr(request, "path", "") or "/"
    return {
        "next_tr": path_for_language(path, "tr"),
        "next_en": path_for_language(path, "en"),
        "next_de": path_for_language(path, "de"),
    }


def site_settings(request):
    """Tüm şablonlarda site_settings (Genel Bilgiler) kullanılır."""
    return {"site_settings": SiteSettings.get_singleton()}


def site_images(request):
    """Tüm şablonlarda site_images (admin'den yüklenen veya varsayılan görseller) kullanılır."""
    from .image_utils import get_site_images
    return {"site_images": get_site_images(request)}
