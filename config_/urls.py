from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = []

urlpatterns += i18n_patterns(
    path('secure-admin-portal/', admin.site.urls),
    path('', include('gt_backend.urls')),
)

handler404 = 'gt_backend.views.NF404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)