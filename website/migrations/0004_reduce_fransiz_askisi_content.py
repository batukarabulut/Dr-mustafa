# Sadece kullanılan 18 anahtarı bırak, diğer fransiz_askisi_* kayıtlarını sil

from django.db import migrations

KEEP_SLUGS = [
    "fransiz_askisi_page_title",
    "fransiz_askisi_hero_title",
    "fransiz_askisi_hero_subtitle",
    "fransiz_askisi_hero_description",
    "fransiz_askisi_cta_consultation",
    "fransiz_askisi_cta_process",
    "fransiz_askisi_about_title",
    "fransiz_askisi_about_lead",
    "fransiz_askisi_about_paragraph",
    "fransiz_askisi_process_title",
    "fransiz_askisi_process_subtitle",
    "fransiz_askisi_benefits_title",
    "fransiz_askisi_benefits_lead",
    "fransiz_askisi_faq_title",
    "fransiz_askisi_faq_subtitle",
    "fransiz_askisi_cta_section_title",
    "fransiz_askisi_cta_section_lead",
    "fransiz_askisi_cta_disclaimer",
]


def remove_unused(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    TranslatableContent.objects.filter(slug__startswith="fransiz_askisi_").exclude(
        slug__in=KEEP_SLUGS
    ).delete()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_contact_submission"),
    ]

    operations = [
        migrations.RunPython(remove_unused, noop),
    ]
