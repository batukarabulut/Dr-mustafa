from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Estetik cerrahi
    path('estetik-cerrahi/rinoplasti/', views.rinoplasti, name='rinoplasti'),
    path('estetik-cerrahi/meme-estetigi/', views.meme_estetigi, name='meme_estetigi'),
    path('estetik-cerrahi/yuz-estetigi/', views.yuz_estetigi, name='yuz_estetigi'),
    path('estetik-cerrahi/vucut-estetigi/', views.vucut_estetigi, name='vucut_estetigi'),
    path('estetik-cerrahi/jinekomasti/', views.jinekomasti, name='jinekomasti'),

    # Ameliyatsız estetik
    path('ameliyatsiz-estetik/botoks/', views.botoks, name='botoks'),
    path('ameliyatsiz-estetik/dolgu/', views.dolgu, name='dolgu'),
    path('ameliyatsiz-estetik/fransiz-askisi/', views.fransiz_askisi, name='fransiz_askisi'),
    path('ameliyatsiz-estetik/mezoterapi/', views.mezoterapi, name='mezoterapi'),
    path('ameliyatsiz-estetik/prp/', views.prp, name='prp'),

    # Medya
    path('media/', views.media, name='media'),
]
