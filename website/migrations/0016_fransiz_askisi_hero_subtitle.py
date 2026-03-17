# Fransız Askısı hero alt başlığını admin panelinden düzenlenebilir yapmak için seed

from django.db import migrations


def seed_hero_subtitle(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    TranslatableContent.objects.get_or_create(
        slug="fransiz_askisi_hero_subtitle",
        defaults={
            "label": "Fransız Askısı – Hero alt başlık",
            "content_tr": "Emilir ipliklerle doğal yüz germe ve sıkılaştırma. Ameliyatsız çözüm.",
        },
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0015_fransiz_askisi_ek_faydalari"),
    ]

    operations = [
        migrations.RunPython(seed_hero_subtitle, noop),
    ]
