from django.contrib import admin, messages
from django.contrib.admin import register

from .models import HyperParameter
from .services import HyperParameterUpdateFailed, update_hyperparam


@register(HyperParameter)
class HyperParameterAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created_at", "updated_at"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        try:
            update_hyperparam(obj)
        except HyperParameterUpdateFailed as e:
            messages.error(request, str(e))


admin.site.site_header = "Bittensor Administration Panel"
admin.site.site_title = "Bittensor Administration Panel"
admin.site.index_title = "Welcome to Bittensor Administration Panel"
