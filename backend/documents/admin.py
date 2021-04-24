from django.contrib import admin
from .models import Document, Pattern, Field


class FieldInline(admin.TabularInline):
    model = Field
    extra = 0


class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        FieldInline,
    ]


admin.site.register(Document, DocumentAdmin)
admin.site.register(Pattern)
admin.site.register(Field)
