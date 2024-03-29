"""eval_iii_FabricioCayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from mundial_app.views import puntoProtegidoEjemplo
from .views import login, userLogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mundial_api.urls')),
    path('api/auth/', login),
    path('api/test-protegido/', puntoProtegidoEjemplo),
    path('api/logout/', userLogout),
    path('app/', include('mundial_app.urls')),

]
