from django.conf.urls import include, url
from django.urls import re_path
from django.contrib import admin
from django.conf.urls.static import static
from geoserver import settings
from semantics import urls as semantics_urls
from labels import urls as labels_urls
from questions import urls as questions_urls

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'geoserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^semantics/', include(semantics_urls)),
    re_path(r'^labels/', include(labels_urls)),
    re_path(r'^questions/', include(questions_urls)),
    re_path(r'^admin/', admin.site.urls),
]

if settings.local.DEBUG:
    urlpatterns += static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
    urlpatterns += static(settings.local.STATIC_URL, document_root=settings.local.STATIC_ROOT)
