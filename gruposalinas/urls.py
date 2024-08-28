"""
URL configuration for gruposalinas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from agenda.api.router import router_agenda
from usuarioagendas.api.router import router_usuario
from .view import inicio


url_static_api = "api/"

urlpatterns = [
    path('', inicio, name='home'),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Esquema OpenAPI
    path('schema-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(url_static_api, include(router_usuario.urls)),
    path(url_static_api, include(router_agenda.urls))
]

urlpatterns += [
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
