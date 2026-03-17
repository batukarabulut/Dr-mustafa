# Instagram URL'ini güncelle: @plasticsurgeon.mustafaoksuz

from django.db import migrations


def update_instagram_url(apps, schema_editor):
    SiteSettings = apps.get_model("website", "SiteSettings")
    obj = SiteSettings.objects.filter(pk=1).first()
    if obj:
        obj.instagram_url = "https://www.instagram.com/plasticsurgeon.mustafaoksuz/"
        obj.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0016_fransiz_askisi_hero_subtitle"),
    ]

    operations = [
        migrations.RunPython(update_instagram_url, noop),
    ]
