# Hakkımda: Aydın Medinova 2025 sonlandırma + hero/card görselleri düzenlenebilir

from django.db import migrations


UPDATED_EXPERIENCE_1 = (
    "2018 yılından itibaren İzmir Özel Gazi Hastanesi'nde özellikle meme estetiği, meme dikleştirme, meme protezi ile büyütme, burun estetiği, liposuction, karın germe, jinekomasti, yüz ve boyun germe, üst ve alt göz kapağı estetiği, şakak germe, dermal dolgu, dudak dolgusu ve botoks uygulamaları başta olmak üzere yoğun şekilde estetik cerrahi operasyonları yapmaktadır. Halen Özel İzmir Gazi Hastanesi'nde estetik cerrahi operasyonlar ile botoks/dolgu uygulamaları gerçekleştirmektedir. Özel Aydın Medinova Hastaneleri'ndeki görevi 2025'te sona ermiştir."
)


def seed_about_images(apps, schema_editor):
    SiteImage = apps.get_model("website", "SiteImage")
    SiteImage.objects.get_or_create(
        key="about_hero",
        defaults={"label": "Hakkımda – Ana Görsel"},
    )
    SiteImage.objects.get_or_create(
        key="about_card",
        defaults={"label": "Hakkımda – Bilgi Kartı Görseli"},
    )

    # Mesleki deneyim metnini güncelle (Aydın Medinova 2025 sonlandırma)
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    obj = TranslatableContent.objects.filter(slug="about_experience_1").first()
    if obj:
        obj.content_tr = UPDATED_EXPERIENCE_1
        obj.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_update_instagram_url"),
    ]

    operations = [
        migrations.RunPython(seed_about_images, noop),
    ]
