from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', include('auto.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui as URLs de autenticação do Django
    path('', RedirectView.as_view(url='/auto/', permanent=True)),  # Redirecionamento para a página inicial
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)