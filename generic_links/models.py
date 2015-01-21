from django.db import models
from django.conf import settings
import numconv


class GenericLink(models.Model):
    where = models.CharField(max_length=200, blank=True, default="")
    url = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    show_in_admin = models.BooleanField(default=True)
    rotate = models.CharField(max_length=100, blank=True)  # comma separated IDs

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_link(self):
        quick_id = numconv.int2str(int(self.id), 32, numconv.BASE32)
        return "/glc/%s/" % quick_id

    def get_full_url(self):
        return settings.DOMAIN + self.get_link()

    def get_click_count(self):
        return GenericLinkClick.objects.filter(link=self).count()


class GenericLinkClick(models.Model):
    link = models.ForeignKey('GenericLink')
    ip = models.IPAddressField()
    created = models.DateTimeField(auto_now_add=True)
