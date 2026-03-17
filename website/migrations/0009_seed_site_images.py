# Data migration: Site görseli anahtarlarını oluştur (admin'de listelensin)

from django.db import migrations


IMAGE_KEYS = [
    ("logo", "Logo"),
    ("mainpage1", "Anasayfa / Hakkımda görsel 1"),
    ("mainpage2", "Anasayfa görsel 2"),
    ("rinoplasti", "Rinoplasti sayfa görseli"),
    ("rinoplasti_process", "Rinoplasti süreç görseli"),
    ("dolgu_card", "Dolgu kart görseli"),
    ("botoks_card", "Botoks kart görseli"),
    ("mezoterapi_card", "Mezoterapi kart görseli"),
    ("prp_card", "PRP kart görseli (anasayfa)"),
    ("prp_photo", "PRP / Mezoterapi sayfa görseli"),
    ("fransiz_askisi", "Fransız Askısı sayfa görseli"),
    ("fransiz_askisi_process", "Fransız Askısı süreç görseli"),
    ("meme_estetigi_card", "Meme estetiği kart görseli"),
    ("yuz_estetigi_card", "Yüz estetiği kart görseli"),
    ("vucut_estetigi_card", "Vücut estetiği kart görseli"),
]


def create_site_image_keys(apps, schema_editor):
    SiteImage = apps.get_model("website", "SiteImage")
    for key, label in IMAGE_KEYS:
        SiteImage.objects.get_or_create(key=key, defaults={"label": label})


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_site_image'),
    ]

    operations = [
        migrations.RunPython(create_site_image_keys, noop),
    ]
