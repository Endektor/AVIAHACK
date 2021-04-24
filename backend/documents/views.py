from django.shortcuts import render
from rest_framework import generics, mixins

from docx2pdf import convert

from .models import Document
from .serializers import DocumentSerializer


class GetConfirmDocument(generics.RetrieveUpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'id'

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
