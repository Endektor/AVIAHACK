from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from documents import views as documents_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/document/(?P<id>[0-9]+)$', documents_views.GetConfirmDocument.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns.append(url(r'^', documents_views.ReactAppView.as_view()))
