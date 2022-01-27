from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user management
    path('accounts/', include('allauth.urls')),
    # local
    path('', include('paginas.urls', namespace='paginas')),
    path('', include('usuarios.urls', namespace='usuarios')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
