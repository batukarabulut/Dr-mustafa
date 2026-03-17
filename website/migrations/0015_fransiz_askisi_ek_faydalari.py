# İplik Türleri -> Ek Faydaları: Mevcut verileri güncelle

from django.db import migrations


def update_to_ek_faydalari(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    updates = {
        "fransiz_askisi_about_thread_types_title": ("Ek Faydaları", "Fransız Askısı – Ek faydalar başlık"),
        "fransiz_askisi_about_thread_1": ("Anında germe ve sıkılaştırma etkisi", "Fransız Askısı – Ek fayda 1"),
        "fransiz_askisi_about_thread_2": ("Doğal kolajen üretimi ile uzun süreli sonuç", "Fransız Askısı – Ek fayda 2"),
        "fransiz_askisi_about_thread_3": ("Minimal risk, kısa iyileşme süresi", "Fransız Askısı – Ek fayda 3"),
        "fransiz_askisi_about_thread_4": ("Kişiye özel tedavi planı", "Fransız Askısı – Ek fayda 4"),
    }
    for slug, (content_tr, label) in updates.items():
        obj = TranslatableContent.objects.filter(slug=slug).first()
        if obj:
            obj.content_tr = content_tr
            obj.label = label
            obj.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0014_seed_faq_questions"),
    ]

    operations = [
        migrations.RunPython(update_to_ek_faydalari, noop),
    ]
