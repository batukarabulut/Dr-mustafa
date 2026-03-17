# Seed home, about, contact and service page content keys (TR defaults)

from django.db import migrations


def seed(apps, schema_editor):
    SiteSettings = apps.get_model("website", "SiteSettings")
    TranslatableContent = apps.get_model("website", "TranslatableContent")

    SiteSettings.objects.get_or_create(pk=1, defaults={"doctor_name": "Op. Dr. Mustafa Öksüz"})

    items = [
        ("home_", [
            ("hero_lead", "Anasayfa hero metni", "15 yıllık deneyim ve son teknoloji ile plastik cerrahi alanında size en iyi hizmeti sunuyoruz. Güvenilir ve estetik sonuçlar için bizimle iletişime geçin."),
            ("about_lead", "Anasayfa hakkında metni", "15 yıllık deneyimim ile plastik ve rekonstrüktif cerrahi alanında uzmanlaştım. Hastalarımın güvenliğini ve memnuniyetini her şeyin önünde tutarak, en güncel tekniklerle doğal ve estetik sonuçlar elde etmeyi hedefliyorum."),
        ]),
        ("about_", [
            ("experience_1", "Hakkımızda deneyim 1", "2018 yılından itibaren İzmir Özel Gazi Hastanesi'nde özellikle meme estetiği, meme dikleştirme, meme protezi ile büyütme, burun estetiği, liposuction, karın germe, jinekomasti, yüz ve boyun germe, üst ve alt göz kapağı estetiği, şakak germe, dermal dolgu, dudak dolgusu ve botoks uygulamaları başta olmak üzere yoğun şekilde estetik cerrahi operasyonları yapmaktadır. Halen Özel İzmir Gazi Hastanesi ve Özel Aydın Medinova Hastaneleri'nde estetik cerrahi operasyonlar ile botoks/dolgu uygulamaları gerçekleştirmektedir."),
            ("experience_2", "Hakkımızda deneyim 2", "Türk Plastik Cerrahi Derneği Yeterlilik (Board Sınavı) Belgesine sahiptir. Türk Plastik Cerrahi Derneği ve Estetik Plastik Cerrahi Derneği'nin tam üyesidir. Halen Türk Plastik Cerrahi Derneği Saç Ekimi Bilim Kurulu üyesi olup, Ekim 2020-2022 yılları arasında Türk Tabipleri Birliği İzmir Hekim Meclisi'nde delegelik görevini yürütmüştür. Evli ve 3 çocuk babasıdır."),
        ]),
        ("contact_", [
            ("intro", "İletişim giriş metni", "Randevu ve bilgi için aşağıdaki formu doldurabilir veya doğrudan iletişime geçebilirsiniz."),
        ]),
    ]
    for prefix, pairs in items:
        for suffix, label, content_tr in pairs:
            slug = prefix + suffix
            TranslatableContent.objects.get_or_create(slug=slug, defaults={"label": label, "content_tr": content_tr})

    # Service pages: same key set for each
    service_keys = [
        "about_lead", "about_paragraph",
        "process_step_1_desc", "process_step_2_desc", "process_step_3_desc",
        "process_step_4_desc", "process_step_5_desc", "process_step_6_desc",
        "benefits_lead", "benefit_1_desc", "benefit_2_desc", "benefit_3_desc", "benefit_4_desc",
        "faq_1_a", "faq_2_a", "faq_3_a", "faq_4_a", "faq_5_a",
        "cta_section_lead", "cta_disclaimer",
    ]
    service_data = {
        "rinoplasti_": (
            "Rinoplasti",
            ["Rinoplasti, burun estetiği olarak da bilinen, burnun şeklini ve işlevini iyileştirmek için yapılan cerrahi bir işlemdir.",
             "Modern rinoplasti tekniklerinde amaç, hastanın yüz yapısına en uygun, doğal görünümlü bir burun elde etmektir. Sadece estetik kaygılarla değil, nefes alma problemlerinin çözümü için de uygulanabilir.",
             "Detaylı muayene ve 3D simülasyon ile ameliyat planlaması yapılır. Beklentileriniz ve tıbbi durumunuz değerlendirilir.",
             "Gerekli tetkikler yapılır. Ameliyat günü ve sonrasına dair detaylı bilgilendirme alırsınız.",
             "1-2 saat süren ameliyat genel anestezi altında gerçekleştirilir. Modern kapalı teknik kullanılır.",
             "7-10 gün burun teli ile koruma. Düzenli kontroller ile iyileşme süreci takip edilir.",
             "3-6 ayda şekil oturur, 1 yılda final sonuç elde edilir. Yaşam boyu garanti verilir.",
             "Düzenli kontroller ile iyileşme süreci izlenir. 7/24 iletişim desteği sağlanır.",
             "Rinoplasti sadece estetik bir işlem değil, aynı zamanda işlevsel sorunları da çözen kapsamlı bir cerrahi müdahaledir.",
             "Yüz ile uyumlu, doğal görünümlü burun şekli", "Septum deviasyonu ve burun tıkanıklığı çözümü",
             "Kişisel memnuniyet ve sosyal güven artışı", "Yaşam boyu sürecek doğal ve estetik görünüm",
             "Rinoplasti ameliyatı genel anestezi altında yapıldığı için ameliyat sırasında hiçbir ağrı hissetmezsiniz. Ameliyat sonrası ağrı çok minimal düzeydedir ve verilen ağrı kesicilerle rahatça kontrol edilebilir.",
             "Ofis işi yapıyorsanız 7-10 gün sonra işinize dönebilirsiniz. Ağır spor ve fiziksel aktiviteler için 6-8 hafta beklemeniz gerekir. Sosyal aktivitelere 2 hafta sonra katılabilirsiniz.",
             "Rinoplasti kalıcı bir işlemdir. Burun yaşam boyu yeni şeklini korur; ek ameliyat sadece travma veya özel istek durumunda gündeme gelir.",
             "Genel anestezi kullanılır; ameliyat sırasında hiçbir şey hissetmezsiniz. Ameliyat sonrası ilk günlerde hafif ağrı olabilir, ağrı kesicilerle kontrol edilir.",
             "Ameliyat 1-2 saat sürer. Hastanede genellikle 1 gece kalınır, ertesi gün taburcu edilirsiniz.",
             "Rinoplasti ile ilgili tüm sorularınızı yanıtlayalım", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"]),
        "dolgu_": (
            "Dolgu",
            ["Dolgu uygulamaları, hyaluronik asit gibi güvenli maddelerle yüzün çeşitli bölgelerine hacim kazandırma, şekillendirme ve yaşlanma belirtilerini azaltma işlemidir.",
             "Bu uygulamalar sayesinde dudaklar dolgunlaştırılabilir, yanak kontuları belirginleştirilebilir, çene hatları şekillendirilebilir ve çeşitli yaşlanma çizgileri doldurulabilir. Sonuçlar anında görülür ve doğal görünür.",
             "Yüz analizi yapılır ve uygun dolgu türü belirlenir. Beklentiler ve uygulama planı değerlendirilir.",
             "Cilt temizlenir ve topikal anestezi uygulanır. Enjeksiyon noktaları işaretlenir.",
             "20-45 dakika süren uygulama. Hassas tekniklerle doğal görünüm elde edilir.",
             "Hafif ödem ve kızarıklık normal. Sonuç anında görülür ve günlük hayata dönülür.",
             "1-2 hafta içinde ödem geçer ve final şekil alır. Doğal görünüm elde edilir.",
             "Etki 9-18 ay sürer. Düzenli kontroller ve gerekirse yenileme uygulaması yapılır.",
             "Dolgu uygulamaları güvenli, etkili ve anında sonuç veren ameliyatsız estetik çözümlerdir. Doğal görünüm elde etmenin en pratik yoludur.",
             "Uygulama sonrası hemen görünür etki", "Abartısız, doğal hacim artışı", "FDA onaylı, biyouyumlu dolgu", "9-18 ay süren kalıcı sonuç",
             "İşlem topikal krem veya lokal anestezi ile yapılır. Hafif batma hissi olabilir, ağrı minimal düzeydedir.",
             "Etki 9-18 ay sürer; dolgu türüne ve uygulama bölgesine göre değişir. Düzenli uygulama ile uzun süre korunabilir.",
             "Hyaluronik asit dolgular FDA onaylı ve vücut tarafından zamanla emilir. Alerji riski çok düşüktür.",
             "Ertesi gün normal hayatınıza dönebilirsiniz. Birkaç gün ağır mimik ve masajdan kaçınmanız önerilir.",
             "Dudak, yanak, çene, burun kökü, nazolabial çizgiler ve el dorsumu gibi birçok bölgeye uygulanabilir.",
             "Dolgu uygulamaları ile ilgili tüm sorularınızı yanıtlayalım", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"]),
        "botoks_": (
            "Botoks",
            ["Botoks, yüzdeki kırışıklıkları azaltmak ve önlemek için kullanılan, klinik olarak kanıtlanmış güvenli bir uygulamadır.",
             "Botulinum toksin enjeksiyonu, mimik kaslarını geçici olarak gevşeterek kaş çatma çizgileri, alın kırışıklıkları ve göz çevresi kırışıklıklarını yumuşatır. Uygulama 10-15 dakika sürer ve anında günlük hayata dönülür.",
             "Yüz analizi ve hedeflenen bölgeler belirlenir. Beklentileriniz değerlendirilir.", "Cilt temizlenir. Gerekirse topikal anestezi uygulanır.",
             "İnce iğnelerle hedef bölgelere enjeksiyon yapılır. İşlem 10-15 dakika sürer.",
             "Hafif kızarıklık veya küçük morluklar olabilir. Birkaç gün içinde kaybolur.",
             "3-7 gün içinde etki belirginleşir. 2 haftada tam sonuç görülür.", "Etki 3-6 ay sürer. Düzenli uygulama ile daha uzun süre korunabilir.",
             "Botoks, ameliyatsız kırışıklık tedavisinde en çok tercih edilen yöntemdir. Hızlı, güvenli ve doğal sonuç verir.",
             "Kaş çatma ve alın kırışıklıklarında belirgin azalma", "Göz çevresi (kaz ayağı) kırışıklıklarının yumuşaması",
             "Önleyici tedavi ile yeni kırışıklıkların geciktirilmesi", "Hızlı uygulama, kısa iyileşme süresi",
             "İşlem ince iğnelerle yapılır; çoğu hastada anestezi gerekmez. Hafif batma hissi olabilir.",
             "Etki 3-6 ay sürer. Düzenli uygulama ile süre uzayabilir.",
             "Botoks on yıllardır kullanılan, FDA onaylı güvenli bir üründür. Doğru doz ve teknikle yan etki riski çok düşüktür.",
             "Aynı gün makyaj yapılabilir; 6 saat yüzü yıkamamanız ve masaj yapmamanız önerilir.",
             "Alın, kaş arası ve göz çevresi en sık uygulama bölgeleridir. Boyun ve çene bölgesi de uygulanabilir.",
             "Botoks uygulaması ile ilgili tüm sorularınızı yanıtlayalım", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"]),
        "mezoterapi_": (
            "Mezoterapi",
            ["Mezoterapi, cilt ve saç problemlerini tedavi etmek için vitamin, mineral ve hyaluronik asit gibi maddelerin ince iğnelerle cilt altına uygulandığı bir yöntemdir.",
             "Yüz mezoterapisi cildi nemlendirir, canlılık kazandırır ve ince kırışıklıkları azaltır. Saç mezoterapisi ise saç dökülmesini yavaşlatır ve saç kalitesini artırır. Uygulama 15-30 dakika sürer.",
             "Cilt veya saç analizi yapılır. Uygun kokteyl ve bölgeler belirlenir.", "Cilt temizlenir. Gerekirse topikal anestezi uygulanır.",
             "İnce iğnelerle küçük dozlar halinde uygulama yapılır. 15-30 dakika sürer.",
             "Hafif kızarıklık ve küçük kabarcıklar normaldir. Birkaç saat içinde geçer.",
             "Birkaç seans sonrası cilt parlaklığı ve nem artar. Saçta 2-3 ay içinde etki görülür.",
             "Düzenli seanslarla sonuçlar kalıcı hale getirilebilir. Önerilen aralık 2-4 hafta.",
             "Mezoterapi hem cilt hem saç için doğal, ameliyatsız bir tedavi seçeneğidir. Minimal risk ve kısa iyileşme süresi sunar.",
             "Cilt nemi ve parlaklığında artış", "İnce kırışıklıkların azalması", "Saç dökülmesinin yavaşlaması", "Kolajen ve elastin uyarımı",
             "İnce iğneler kullanılır; çoğu hastada tolere edilebilir. Topikal anestezi ile rahatlık sağlanabilir.",
             "Cilt için 4-6 seans, saç için 8-10 seans önerilir. Aralık 2-4 hafta olabilir.",
             "Evet. Mezoterapi doğal maddeler kullanır; alerji öyküsüne göre içerik ayarlanır.",
             "Aynı gün makyaj yapılabilir. Birkaç saat güneşten ve sıcaktan kaçınmanız önerilir.",
             "Yüz, boyun, dekolte, saçlı deri ve el dorsumu en sık uygulama bölgeleridir.",
             "Mezoterapi ile ilgili tüm sorularınızı yanıtlayalım", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"]),
        "prp_": (
            "PRP",
            ["PRP (Platelet Rich Plasma), kendi kanınızdan elde edilen trombosit zengin plazmanın cilt veya saç bölgesine enjekte edildiği yenileyici bir tedavidir.",
             "Trombositler büyüme faktörleri içerir; bu da ciltte kolajen üretimini artırır, saç foliküllerini güçlendirir. Tamamen doğal ve kişiye özel bir yöntemdir. Yüz gençleştirme, saç dökülmesi ve cilt kalitesi artırmada kullanılır.",
             "Kan alınır ve özel tüplerde santrifüj edilir. PRP ayrıştırılır.", "Cilt veya saçlı deri temizlenir. Uygulama bölgeleri belirlenir.",
             "PRP ince iğnelerle cilt altına veya saçlı deriye uygulanır. 20-30 dakika sürer.",
             "Hafif kızarıklık ve şişlik normaldir. 1-2 gün içinde azalır.",
             "2-4 hafta içinde ciltte parlaklık ve sıkılık artar. Saçta 2-3 ay içinde etki görülür.",
             "3-4 seanslık kür önerilir. Yılda bir tekrar ile sonuçlar korunabilir.",
             "PRP tamamen kendi kanınızdan üretildiği için alerji riski yoktur. Cilt ve saç için doğal yenilenme sağlar.",
             "Ciltte kolajen artışı ve sıkılaşma", "Saç kalitesi ve yoğunluğunda artış", "Doğal, kişiye özel tedavi", "Minimal risk, kısa iyileşme süresi",
             "Önce kolunuzdan az miktarda kan alınır. PRP ayrıştırıldıktan sonra ince iğnelerle uygulama yapılır. Hafif batma hissi olabilir.",
             "Cilt için 3-4 seans, saç için 4-6 seans önerilir. Aralık 3-4 hafta olabilir.",
             "Evet. Kendi kanınızdan elde edildiği için alerji ve red reaksiyonu riski yoktur.",
             "1-2 gün hafif kızarıklık olabilir. Makyaj ertesi gün yapılabilir.",
             "Yüz, boyun, dekolte, el dorsumu ve saçlı deri en sık uygulama bölgeleridir.",
             "PRP tedavisi ile ilgili tüm sorularınızı yanıtlayalım", "Konsültasyonunuz tamamen ücretsiz ve yükümlülük gerektirmez"]),
    }
    for prefix, (page_name, contents) in service_data.items():
        for i, key in enumerate(service_keys):
            if i < len(contents):
                slug = prefix + key
                label = f"{page_name} – {key}"
                TranslatableContent.objects.get_or_create(slug=slug, defaults={"label": label, "content_tr": contents[i]})


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("website", "0006_site_settings_and_proxies")]
    operations = [migrations.RunPython(seed, noop)]
