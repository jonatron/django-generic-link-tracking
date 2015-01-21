from django.contrib import admin
from .models import GenericLink


class GenericLinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericLink, GenericLinkAdmin)
