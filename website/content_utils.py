from .models import TranslatableContent


def get_content_map(request, prefix):
    """
    Veritabanındaki TranslatableContent kayıtlarından prefix ile başlayanları
    seçer; dil için get_for_language ile içeriği döndürür.
    Dönen sözlük: short_key -> içerik (örn. hero_title -> "Fransız Askısı").
    """
    lang = (getattr(request, "LANGUAGE_CODE", None) or "tr")[:2].lower()
    qs = TranslatableContent.objects.filter(slug__startswith=prefix)
    result = {}
    for row in qs:
        short_key = row.slug[len(prefix) :] if row.slug.startswith(prefix) else row.slug
        result[short_key] = row.get_for_language(lang)
    return result


def get_page_content(request, prefix, defaults):
    """
    Sayfa içeriğini döndürür: önce DB'den prefix ile yüklenir,
    boş olan anahtarlar defaults ile doldurulur (TR fallback).
    """
    db = get_content_map(request, prefix)
    merged = dict(defaults)
    for key, value in db.items():
        if value:
            merged[key] = value
    return merged
