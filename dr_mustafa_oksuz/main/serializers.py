from rest_framework import serializers
from .models import ContactSubmission

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message']
        
    def create(self, validated_data):
        # is_read otomatik False olarak ayarlanır
        return ContactSubmission.objects.create(**validated_data)