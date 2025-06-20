from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response({
                'message': 'Mesajınız başarıyla gönderildi!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)