# Mezoterapi hero alt başlığını admin panelinden düzenlenebilir yapmak için seed

from django.db import migrations


def seed_hero_subtitle(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    TranslatableContent.objects.get_or_create(
        slug="mezoterapi_hero_subtitle",
        defaults={
            "label": "Mezoterapi – Hero alt başlık",
            "content_tr": "Vitamin, mineral ve aktif maddelerle cilt gençleştirme. İşlem sadece 15-30 dakika sürer.",
        },
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_seed_botoks_hero"),
    ]

    operations = [
        migrations.RunPython(seed_hero_subtitle, noop),
    ]
