from django.shortcuts import render
from rest_framework import generics, mixins
from django.utils import timezone
from django.core.mail import EmailMessage

from docx2pdf import convert

from .models import Document
from .serializers import DocumentSerializer


class GetConfirmDocument(generics.RetrieveUpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'id'
    
    
    def send_document(self, obj,  email):
        email = EmailMessage("Document", "Document", "paul@polo.com", (email,))
        email.content_subtype = "html"

        fd = open(obj.document.path, 'rb')
        email.attach('document.pdf', fd.read(), 'application/pdf')
        email.send()

    def put(self, request, *args, **kwargs):
        obj_id = kwargs.get('id')
        obj = self.queryset.get(id=obj_id)
        obj.confirmed_datetime = timezone.now()
        obj.save()
        self.send_document(obj, request.data.get('email'))
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        obj_id = kwargs.get('id')
        obj = self.queryset.get(id=obj_id)
        obj.confirmed_datetime = timezone.now()
        obj.save()
        self.send_document(obj, request.data.get('email'))
        return self.partial_update(request, *args, **kwargs)

