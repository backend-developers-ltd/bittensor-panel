from django.conf import settings
from django.contrib.admin.sites import site
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", site.urls),
    path("", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(url=reverse_lazy("admin:core_hyperparameter_changelist"))),
]

if settings.DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
