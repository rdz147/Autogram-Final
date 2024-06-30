# meu_projeto/urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', include('auto.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/auto/', permanent=True)),  # Adicionado
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
