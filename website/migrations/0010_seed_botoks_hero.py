# Add botoks_hero image key for hero section

from django.db import migrations


def add_botoks_hero(apps, schema_editor):
    SiteImage = apps.get_model("website", "SiteImage")
    SiteImage.objects.get_or_create(
        key="botoks_hero",
        defaults={"label": "Botoks sayfası hero görseli (yatay)"},
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_seed_site_images'),
    ]

    operations = [
        migrations.RunPython(add_botoks_hero, noop),
    ]
