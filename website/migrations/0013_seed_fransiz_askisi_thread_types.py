# Fransız Askısı İplik Türleri bölümünü admin panelinden düzenlenebilir yapmak için seed

from django.db import migrations


def seed_thread_types(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    items = [
        ("about_thread_types_title", "İplik Türleri", "Fransız Askısı – İplik türleri başlık"),
        ("about_thread_1", "PDO Mono iplikler", "Fransız Askısı – İplik türü 1"),
        ("about_thread_2", "PDO Cog iplikler", "Fransız Askısı – İplik türü 2"),
        ("about_thread_3", "PCL iplikler", "Fransız Askısı – İplik türü 3"),
        ("about_thread_4", "PLLA iplikler", "Fransız Askısı – İplik türü 4"),
    ]
    for suffix, content_tr, label in items:
        slug = f"fransiz_askisi_{suffix}"
        TranslatableContent.objects.get_or_create(
            slug=slug,
            defaults={"label": label, "content_tr": content_tr},
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_seed_mezoterapi_hero_motto"),
    ]

    operations = [
        migrations.RunPython(seed_thread_types, noop),
    ]
