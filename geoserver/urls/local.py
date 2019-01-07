from django.conf.urls import include, url

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

    url(r'^semantics/', include(semantics_urls)),
    url(r'^labels/', include(labels_urls)),
    url(r'^questions/', include(questions_urls)),
    url(r'^admin/', admin.site.urls),
]

if settings.local.DEBUG:
    urlpatterns += static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
    urlpatterns += static(settings.local.STATIC_URL, document_root=settings.local.STATIC_ROOT)
