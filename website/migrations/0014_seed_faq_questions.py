# FAQ sorularını admin panelinden düzenlenebilir yapmak için tüm sayfalara seed

from django.db import migrations

# (prefix, page_label) -> [(suffix, content_tr, label)]
FAQ_QUESTIONS_DATA = {
    "fransiz_askisi_": ("Fransız Askısı", [
        ("faq_1_q", "Fransız askısı ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Fransız askısı etkisi ne kadar sürer?", "SSS 2 soru"),
        ("faq_3_q", "PDO iplikler güvenli midir?", "SSS 3 soru"),
        ("faq_4_q", "İşlem sonrası ne zaman normale dönerim?", "SSS 4 soru"),
        ("faq_5_q", "Hangi yaşta fransız askısı yapılabilir?", "SSS 5 soru"),
    ]),
    "rinoplasti_": ("Rinoplasti", [
        ("faq_1_q", "Rinoplasti ameliyatı ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Ne zaman normal hayatıma dönebilirim?", "SSS 2 soru"),
        ("faq_3_q", "Sonuç ne zaman tam olarak belli olur?", "SSS 3 soru"),
        ("faq_4_q", "Rinoplasti ameliyatının riskleri nelerdir?", "SSS 4 soru"),
        ("faq_5_q", "Fiyat nedir ve ne kadar sürer?", "SSS 5 soru"),
    ]),
    "dolgu_": ("Dolgu", [
        ("faq_1_q", "Dolgu uygulaması ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Dolgu etkisi ne kadar sürer?", "SSS 2 soru"),
        ("faq_3_q", "Dolgu güvenli midir?", "SSS 3 soru"),
        ("faq_4_q", "Dolgu beğenmezsem ne olur?", "SSS 4 soru"),
        ("faq_5_q", "Dolgu sonrası ne zaman normale dönerim?", "SSS 5 soru"),
    ]),
    "botoks_": ("Botoks", [
        ("faq_1_q", "Botoks uygulaması ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Botoks etkisi ne kadar sürer?", "SSS 2 soru"),
        ("faq_3_q", "Botoks güvenli midir?", "SSS 3 soru"),
        ("faq_4_q", "Botoks sonrası ne zaman normal hayatıma dönebilirim?", "SSS 4 soru"),
        ("faq_5_q", "Hangi yaşta botoks yapılabilir?", "SSS 5 soru"),
    ]),
    "mezoterapi_": ("Mezoterapi", [
        ("faq_1_q", "Mezoterapi ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Kaç seans gerekir?", "SSS 2 soru"),
        ("faq_3_q", "Mezoterapi etkisi ne kadar sürer?", "SSS 3 soru"),
        ("faq_4_q", "Mezoterapi güvenli midir?", "SSS 4 soru"),
        ("faq_5_q", "Hangi bölgelere uygulanır?", "SSS 5 soru"),
    ]),
    "prp_": ("PRP", [
        ("faq_1_q", "PRP tedavisi ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "PRP kaç seans gerektirir?", "SSS 2 soru"),
        ("faq_3_q", "PRP güvenli midir?", "SSS 3 soru"),
        ("faq_4_q", "PRP sonrası iyileşme nasıldır?", "SSS 4 soru"),
        ("faq_5_q", "PRP hangi bölgelere uygulanır?", "SSS 5 soru"),
    ]),
    "meme_estetigi_": ("Meme Estetiği", [
        ("faq_1_q", "Meme büyütme ameliyatı ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "İmplantlar ne kadar süre dayanır?", "SSS 2 soru"),
        ("faq_3_q", "Emzirme üzerinde etkisi var mı?", "SSS 3 soru"),
        ("faq_4_q", "Ameliyat izleri görünür olur mu?", "SSS 4 soru"),
        ("faq_5_q", "Ne zaman spor yapabilirim?", "SSS 5 soru"),
    ]),
    "yuz_estetigi_": ("Yüz Estetiği", [
        ("faq_1_q", "Yüz estetiği ağrılı bir işlem midir?", "SSS 1 soru"),
        ("faq_2_q", "Ne zaman normal aktivitelerime dönebilirim?", "SSS 2 soru"),
        ("faq_3_q", "Yüz estetiği sonuçları ne kadar sürer?", "SSS 3 soru"),
        ("faq_4_q", "Ameliyat izleri görünür olur mu?", "SSS 4 soru"),
        ("faq_5_q", "Hangi yaşta yüz estetiği yaptırabilirim?", "SSS 5 soru"),
    ]),
    "vucut_estetigi_": ("Vücut Estetiği", [
        ("faq_1_q", "Vücut estetiği ameliyatı ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Ne zaman normal aktivitelerime dönebilirim?", "SSS 2 soru"),
        ("faq_3_q", "Vücut estetiği sonuçları kalıcı mıdır?", "SSS 3 soru"),
        ("faq_4_q", "Ameliyat izleri görünür olur mu?", "SSS 4 soru"),
        ("faq_5_q", "Hangi yaşta vücut estetiği yaptırabilirim?", "SSS 5 soru"),
    ]),
    "jinekomasti_": ("Jinekomasti", [
        ("faq_1_q", "Jinekomasti ameliyatı ağrılı mıdır?", "SSS 1 soru"),
        ("faq_2_q", "Ne zaman normale dönebilirim?", "SSS 2 soru"),
        ("faq_3_q", "Jinekomasti tekrar oluşur mu?", "SSS 3 soru"),
        ("faq_4_q", "Ameliyat izleri görünür olur mu?", "SSS 4 soru"),
        ("faq_5_q", "Hangi yaşta jinekomasti ameliyatı olabilirim?", "SSS 5 soru"),
    ]),
}


def seed_faq_questions(apps, schema_editor):
    TranslatableContent = apps.get_model("website", "TranslatableContent")
    for prefix, (page_label, items) in FAQ_QUESTIONS_DATA.items():
        for suffix, content_tr, label_suffix in items:
            slug = prefix + suffix
            label = f"{page_label} – {label_suffix}"
            TranslatableContent.objects.get_or_create(
                slug=slug,
                defaults={"label": label, "content_tr": content_tr},
            )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0013_seed_fransiz_askisi_thread_types"),
    ]

    operations = [
        migrations.RunPython(seed_faq_questions, noop),
    ]
