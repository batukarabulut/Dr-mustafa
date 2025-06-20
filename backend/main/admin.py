from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmission(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter =  ['is_read', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Seçili mesajları okundu olarak işaretle"

    actions = [mark_as_read]


