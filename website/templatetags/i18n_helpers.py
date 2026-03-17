"""
Dil geçişi için yardımcı template tag.

Not: Dil URL'leri context_processors.py'daki language_switch_urls() ile
otomatik olarak şablonlara (next_tr, next_en, next_de) eklenmektedir.
Bu tag doğrudan kullanılmak istenirse mevcuttur.
"""
from django import template

from ..context_processors import path_for_language as _path_for_language

register = template.Library()


@register.simple_tag
def path_for_language(path, lang_code):
    """
    path: request.path (örn. /tr/contact/)
    lang_code: 'tr', 'en', 'de'
    Döner: aynı sayfa, hedef dil prefix ile (örn. /en/contact/)
    """
    return _path_for_language(path, lang_code)
