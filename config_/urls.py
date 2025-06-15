from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = []

urlpatterns += i18n_patterns(
    path('secure-admin-portal/', admin.site.urls),
    path('', include('gt_backend.urls')),
)

handler404 = 'gt_backend.views.NF404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media in development or fallback for production (not for high-traffic prod!)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)