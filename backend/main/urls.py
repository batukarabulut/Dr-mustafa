from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ContactSubmissionViewSet

# DRF router
router = DefaultRouter()
router.register(r'contact', ContactSubmissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]