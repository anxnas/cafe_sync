from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls.api_urls')),
    path('', include('api.urls.web_urls')),
    path('', RedirectView.as_view(url='/order-list/', permanent=True)),
]