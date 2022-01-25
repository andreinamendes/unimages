from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user management
    path('accounts/', include('allauth.urls')),
    # local
    path('', include('paginas.urls', namespace='paginas')),
    path('', include('usuarios.urls', namespace='usuarios')),
]
