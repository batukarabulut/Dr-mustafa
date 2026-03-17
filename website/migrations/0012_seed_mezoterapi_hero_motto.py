# Mezoterapi hero motto metnini admin panelinden düzenlenebilir yapmak için seed

from django.db import migrations


def seed_hero_motto(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    TranslatableContent.objects.get_or_create(
        slug="mezoterapi_hero_motto",
        defaults={
            "label": "Mezoterapi – Hero motto (ana başlık)",
            "content_tr": "Cilt Yenileme,\nMezoterapi ile Mümkün",
        },
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_seed_mezoterapi_hero_subtitle"),
    ]

    operations = [
        migrations.RunPython(seed_hero_motto, noop),
    ]
