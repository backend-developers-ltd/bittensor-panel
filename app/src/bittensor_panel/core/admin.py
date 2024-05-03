from django.contrib import admin  # noqa
from django.contrib.admin import register  # noqa

from .models import HyperParameter


@register(HyperParameter)
class HyperParameterAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created_at", "updated_at"]
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = "Bittensor Administration Panel"
admin.site.site_title = "Bittensor Administration Panel"
admin.site.index_title = "Welcome to Bittensor Administration Panel"
