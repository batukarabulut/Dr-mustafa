# Generated data migration: Fransız Askısı sayfası için TR içerik anahtarları

from django.db import migrations


FRANSIZ_ASKISI_DEFAULTS = {
    "page_title": "Fransız Askısı",
    "hero_title": "Fransız Askısı",
    "hero_subtitle": "PDO Thread Lift ile Ameliyatsız Yüz Germe",
    "hero_description": "Emilir ipliklerle doğal yüz germe ve sıkılaştırma",
    "cta_consultation": "Ücretsiz Konsültasyon",
    "cta_process": "Süreç Hakkında",
    "breadcrumb_home": "Anasayfa",
    "breadcrumb_section": "Ameliyatsız Estetik",
    "breadcrumb_current": "Fransız Askısı",
    "quick_duration_label": "Uygulama Süresi",
    "quick_duration_value": "30-60 Dakika",
    "quick_hospital_label": "Hastanede Kalış",
    "quick_hospital_value": "Yok",
    "quick_anesthesia_label": "Anestezi",
    "quick_anesthesia_value": "Lokal Anestezi",
    "quick_effect_label": "Etki Süresi",
    "quick_effect_value": "12-18 Ay",
    "about_title": "Fransız Askısı Nedir?",
    "about_lead": "Fransız askısı (PDO Thread Lift), emilir iplikler kullanılarak yapılan ameliyatsız yüz germe ve sıkılaştırma işlemidir.",
    "about_paragraph": "Bu yöntemde kullanılan PDO (Polydioxanone) iplikleri cerrahi operasyonlarda da kullanılan güvenli materyallerdir. İplikler cilt altına yerleştirilerek sarkan dokuları yukarı çeker ve kolajen üretimini artırır.",
    "about_areas_title": "Uygulama Alanları",
    "about_area_1": "Yanak ve yanaklık bölgesi",
    "about_area_2": "Çene hattı",
    "about_area_3": "Boyun bölgesi",
    "about_area_4": "Kaş çevresi",
    "about_thread_types_title": "İplik Türleri",
    "about_thread_1": "PDO Mono iplikler",
    "about_thread_2": "PDO Cog iplikler",
    "about_thread_3": "PCL iplikler",
    "about_thread_4": "PLLA iplikler",
    "about_image_alt": "Fransız Askısı Uygulama Süreci",
    "process_title": "Fransız Askısı Uygulama Süreci",
    "process_subtitle": "Konsültasyondan sonuç alana kadar",
    "process_step_1_title": "Detaylı Konsültasyon",
    "process_step_1_desc": "Yüz analizi yapılır ve uygun iplik türü belirlenir. Sarkan bölgeler ve tedavi planı değerlendirilir.",
    "process_step_2_title": "Uygulama Öncesi Hazırlık",
    "process_step_2_desc": "Cilt temizlenir ve lokal anestezi uygulanır. İplik giriş noktaları işaretlenir.",
    "process_step_3_title": "İplik Yerleştirme",
    "process_step_3_desc": "30-60 dakika süren uygulama. İnce kanüller ile iplikler cilt altına yerleştirilir.",
    "process_step_4_title": "Uygulama Sonrası",
    "process_step_4_desc": "Hafif ödem ve morarmalar normaldir. Anında germe etkisi görülür ve günlük hayata dönülür.",
    "process_step_5_title": "İyileşme ve Kolajen Üretimi",
    "process_step_5_desc": "2-4 hafta içinde kolajen üretimi artar. Final etki 2-3 ayda tam olarak görülür.",
    "process_step_6_title": "Uzun Süreli Etki",
    "process_step_6_desc": "Etki 12-18 ay sürer. İplikler tamamen emilir, kolajen etkisi devam eder.",
    "benefits_title": "Neden Fransız Askısı?",
    "benefits_lead": "Fransız askısı ameliyatsız yüz germenin en etkili yöntemidir. Hem anında germe hem de uzun süreli kolajen üretimi sağlar.",
    "benefit_1_title": "Anında Germe",
    "benefit_1_desc": "Uygulama sonrası hemen lifting etkisi",
    "benefit_2_title": "Doğal Sonuç",
    "benefit_2_desc": "Abartısız, doğal germe etkisi",
    "benefit_3_title": "Kolajen Üretimi",
    "benefit_3_desc": "Uzun süreli cilt yenilenmesi",
    "benefit_4_title": "Güvenli Materyal",
    "benefit_4_desc": "Emilir PDO iplikler, minimal risk",
    "faq_title": "Sık Sorulan Sorular",
    "faq_subtitle": "Fransız askısı hakkında merak ettikleriniz",
    "faq_1_q": "Fransız askısı ağrılı mıdır?",
    "faq_1_a": "İşlem lokal anestezi altında yapılır, bu nedenle ağrı hissedilmez. Uygulama sonrası hafif gerginlik hissi olabilir ancak ağrı kesici gerektirecek kadar ağrılı değildir.",
    "faq_2_q": "Fransız askısı etkisi ne kadar sürer?",
    "faq_2_a": "İplik etkisi 12-18 ay sürer. İplikler tamamen emildikten sonra bile, uyardığı kolajen üretimi sayesinde cilt kalitesi uzun süre korunur.",
    "faq_3_q": "PDO iplikler güvenli midir?",
    "faq_3_a": "PDO iplikler uzun yıllardır cerrahide kullanılan güvenli materyallerdir ve vücut tarafından emilir.",
    "faq_4_q": "İşlem sonrası ne zaman normale dönerim?",
    "faq_4_a": "Ertesi gün normal hayatınıza dönebilirsiniz; sadece birkaç gün ağır mimikten ve bir hafta ağır spordan kaçınmanız önerilir.",
    "faq_5_q": "Hangi yaşta fransız askısı yapılabilir?",
    "faq_5_a": "Genellikle 30 yaş üzeri hastalarda uygundur; esas belirleyici olan cilt sarkma derecesi ve beklentilerdir.",
    "cta_section_title": "Ücretsiz Konsültasyon Alın",
    "cta_section_lead": "Fransız askısı ile ilgili tüm sorularınızı yanıtlayalım",
    "cta_phone": "Hemen Ara",
    "cta_appointment": "Randevu Al",
    "cta_disclaimer": "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez",
}


def seed_fransiz_askisi(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    for short_key, content_tr in FRANSIZ_ASKISI_DEFAULTS.items():
        slug = f"fransiz_askisi_{short_key}"
        TranslatableContent.objects.get_or_create(
            slug=slug,
            defaults={"label": f"Fransız Askısı – {short_key}", "content_tr": content_tr},
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_translatable_content"),
    ]

    operations = [
        migrations.RunPython(seed_fransiz_askisi, noop),
    ]
