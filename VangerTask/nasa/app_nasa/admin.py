from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin,admin.ModelAdmin):
    fields = ('name', 'image')
    list_display = ('id', 'get_image', 'name')
    search_fields = ('name',)

    def get_image(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=50>")