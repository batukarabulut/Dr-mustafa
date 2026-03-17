# Eski başlık anahtarlarını kaldır; sadece içerik (paragraf/açıklama) anahtarlarını ekle

from django.db import migrations

# Admin'de düzenlenebilir içerik metinleri (TR varsayılan)
CONTENT_ITEMS = [
    ("fransiz_askisi_about_lead", "Fransız Askısı – Hakkında (lead)", "Fransız askısı (PDO Thread Lift), emilir iplikler kullanılarak yapılan ameliyatsız yüz germe ve sıkılaştırma işlemidir."),
    ("fransiz_askisi_about_paragraph", "Fransız Askısı – Hakkında (paragraf)", "Bu yöntemde kullanılan PDO (Polydioxanone) iplikleri cerrahi operasyonlarda da kullanılan güvenli materyallerdir. İplikler cilt altına yerleştirilerek sarkan dokuları yukarı çeker ve kolajen üretimini artırır."),
    ("fransiz_askisi_process_step_1_desc", "Süreç adım 1 açıklama", "Yüz analizi yapılır ve uygun iplik türü belirlenir. Sarkan bölgeler ve tedavi planı değerlendirilir."),
    ("fransiz_askisi_process_step_2_desc", "Süreç adım 2 açıklama", "Cilt temizlenir ve lokal anestezi uygulanır. İplik giriş noktaları işaretlenir."),
    ("fransiz_askisi_process_step_3_desc", "Süreç adım 3 açıklama", "30-60 dakika süren uygulama. İnce kanüller ile iplikler cilt altına yerleştirilir."),
    ("fransiz_askisi_process_step_4_desc", "Süreç adım 4 açıklama", "Hafif ödem ve morarmalar normaldir. Anında germe etkisi görülür ve günlük hayata dönülür."),
    ("fransiz_askisi_process_step_5_desc", "Süreç adım 5 açıklama", "2-4 hafta içinde kolajen üretimi artar. Final etki 2-3 ayda tam olarak görülür."),
    ("fransiz_askisi_process_step_6_desc", "Süreç adım 6 açıklama", "Etki 12-18 ay sürer. İplikler tamamen emilir, kolajen etkisi devam eder."),
    ("fransiz_askisi_benefits_lead", "Neden Fransız Askısı (paragraf)", "Fransız askısı ameliyatsız yüz germenin en etkili yöntemidir. Hem anında germe hem de uzun süreli kolajen üretimi sağlar."),
    ("fransiz_askisi_benefit_1_desc", "Fayda 1 açıklama", "Uygulama sonrası hemen lifting etkisi"),
    ("fransiz_askisi_benefit_2_desc", "Fayda 2 açıklama", "Abartısız, doğal germe etkisi"),
    ("fransiz_askisi_benefit_3_desc", "Fayda 3 açıklama", "Uzun süreli cilt yenilenmesi"),
    ("fransiz_askisi_benefit_4_desc", "Fayda 4 açıklama", "Emilir PDO iplikler, minimal risk"),
    ("fransiz_askisi_faq_1_a", "SSS 1 cevap", "İşlem lokal anestezi altında yapılır, bu nedenle ağrı hissedilmez. Uygulama sonrası hafif gerginlik hissi olabilir ancak ağrı kesici gerektirecek kadar ağrılı değildir."),
    ("fransiz_askisi_faq_2_a", "SSS 2 cevap", "İplik etkisi 12-18 ay sürer. İplikler tamamen emildikten sonra bile, uyardığı kolajen üretimi sayesinde cilt kalitesi uzun süre korunur."),
    ("fransiz_askisi_faq_3_a", "SSS 3 cevap", "PDO iplikler uzun yıllardır cerrahide kullanılan güvenli materyallerdir ve vücut tarafından emilir."),
    ("fransiz_askisi_faq_4_a", "SSS 4 cevap", "Ertesi gün normal hayatınıza dönebilirsiniz; sadece birkaç gün ağır mimikten ve bir hafta ağır spordan kaçınmanız önerilir."),
    ("fransiz_askisi_faq_5_a", "SSS 5 cevap", "Genellikle 30 yaş üzeri hastalarda uygundur; esas belirleyici olan cilt sarkma derecesi ve beklentilerdir."),
    ("fransiz_askisi_cta_section_lead", "CTA bölümü açıklama", "Fransız askısı ile ilgili tüm sorularınızı yanıtlayalım"),
    ("fransiz_askisi_cta_disclaimer", "CTA yasal uyarı", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"),
]


def replace_with_content_only(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    TranslatableContent.objects.filter(slug__startswith="fransiz_askisi_").delete()
    for slug, label, content_tr in CONTENT_ITEMS:
        TranslatableContent.objects.create(
            slug=slug,
            label=label,
            content_tr=content_tr,
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_reduce_fransiz_askisi_content"),
    ]

    operations = [
        migrations.RunPython(replace_with_content_only, noop),
    ]
