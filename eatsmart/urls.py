from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from tastypie.api import Api
from inspections.api import resources


admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(resources.EstablishmentResource())
v1_api.register(resources.InspectionResource())
v1_api.register(resources.ViolationResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# we need to add the root folder for local debugging to allow the django dev server to serve index.html
if settings.DEBUG:
    urlpatterns += static('/', document_root=settings.PROJECT_ROOT)
