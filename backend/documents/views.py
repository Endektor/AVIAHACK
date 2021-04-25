from django.shortcuts import render
from rest_framework import generics, mixins
from django.utils import timezone
from django.core.mail import EmailMessage
from django.views.generic import View
from django.http import HttpResponse

from docx2pdf import convert
import os

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

class ReactAppView(View):

    def get(self, request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        try:
            with open(os.path.join(BASE_DIR, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )

