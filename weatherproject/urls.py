
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from api import urls as api_urls

urlpatterns = [
	url(r'^', include('weatherapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls, namespace='api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

