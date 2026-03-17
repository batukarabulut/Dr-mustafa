import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import ContactSubmission
from .content_utils import get_page_content
from .content_defaults import (
    FRANSIZ_ASKISI_DEFAULTS,
    HOME_DEFAULTS,
    ABOUT_DEFAULTS,
    CONTACT_DEFAULTS,
    RINOPLASTI_DEFAULTS,
    DOLGU_DEFAULTS,
    BOTOKS_DEFAULTS,
    MEZOTERAPI_DEFAULTS,
    PRP_DEFAULTS,
    MEME_ESTETIGI_DEFAULTS,
    YUZ_ESTETIGI_DEFAULTS,
    VUCUT_ESTETIGI_DEFAULTS,
    JINEKOMASTI_DEFAULTS,
)


def home(request):
    """
    Anasayfa view'i – eski frontend/index.html içeriğinin Django template versiyonu.
    Sayfadaki iletişim formu da burada işlenir (contact ile aynı alanlar).
    """
    success = request.session.pop("contact_success", False)
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactSubmission.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                subject=form.cleaned_data.get("subject") or "",
                message=form.cleaned_data["message"],
                kvkk=form.cleaned_data["kvkk"],
                source="home",
            )
            request.session["contact_success"] = True
            return redirect(reverse("home") + "#contact")
    page_content = get_page_content(request, "home_", HOME_DEFAULTS)
    return render(request, "home.html", {"form": form, "success": success, "page_content": page_content})


def about(request):
    page_content = get_page_content(request, "about_", ABOUT_DEFAULTS)
    return render(request, "about.html", {"page_content": page_content})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactSubmission.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                subject=form.cleaned_data.get("subject") or "",
                message=form.cleaned_data["message"],
                kvkk=form.cleaned_data["kvkk"],
                source="contact",
            )
            request.session["contact_success"] = True
            return redirect(reverse("contact"))
    else:
        form = ContactForm()

    success = request.session.pop("contact_success", False)
    page_content = get_page_content(request, "contact_", CONTACT_DEFAULTS)
    return render(request, "contact.html", {"form": form, "success": success, "page_content": page_content})


def rinoplasti(request):
    page_content = get_page_content(request, "rinoplasti_", RINOPLASTI_DEFAULTS)
    return render(request, "rinoplasti.html", {"page_content": page_content})


def meme_estetigi(request):
    page_content = get_page_content(request, "meme_estetigi_", MEME_ESTETIGI_DEFAULTS)
    return render(request, "meme-estetigi.html", {"page_content": page_content})


def yuz_estetigi(request):
    page_content = get_page_content(request, "yuz_estetigi_", YUZ_ESTETIGI_DEFAULTS)
    return render(request, "yuz-estetigi.html", {"page_content": page_content})


def vucut_estetigi(request):
    page_content = get_page_content(request, "vucut_estetigi_", VUCUT_ESTETIGI_DEFAULTS)
    return render(request, "vucut-estetigi.html", {"page_content": page_content})


def jinekomasti(request):
    page_content = get_page_content(request, "jinekomasti_", JINEKOMASTI_DEFAULTS)
    return render(request, "jinekomasti.html", {"page_content": page_content})


def botoks(request):
    page_content = get_page_content(request, "botoks_", BOTOKS_DEFAULTS)
    return render(request, "botoks.html", {"page_content": page_content})


def dolgu(request):
    page_content = get_page_content(request, "dolgu_", DOLGU_DEFAULTS)
    return render(request, "dolgu.html", {"page_content": page_content})


def fransiz_askisi(request):
    page_content = get_page_content(request, "fransiz_askisi_", FRANSIZ_ASKISI_DEFAULTS)
    return render(
        request,
        "ameliyatsiz-estetik-fransiz-askisi.html",
        {"page_content": page_content},
    )


def mezoterapi(request):
    page_content = get_page_content(request, "mezoterapi_", MEZOTERAPI_DEFAULTS)
    return render(request, "mezoterapi.html", {"page_content": page_content})


def prp(request):
    page_content = get_page_content(request, "prp_", PRP_DEFAULTS)
    return render(request, "prp.html", {"page_content": page_content})


def media(request):
    return render(request, "media.html")


def api_contact(request):
    """
    JSON tabanlı iletişim endpoint'i.
    Mevcut JS (contactForm handler) buraya POST gönderiyor.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    form = ContactForm(data)
    if form.is_valid():
        ContactSubmission.objects.create(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            phone=form.cleaned_data["phone"],
            subject=form.cleaned_data.get("subject") or "",
            message=form.cleaned_data["message"],
            kvkk=form.cleaned_data["kvkk"],
            source="api",
        )
        return JsonResponse({"message": "ok"})

    return JsonResponse({"errors": form.errors}, status=400)
