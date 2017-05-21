"""ark_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from arkapp import views as arkapp_views
from arkapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^minters/$', arkapp_views.minters_list, name='minters_list'),
    url(r'^arks/$', arkapp_views.arks_list, name='arks_list'),
    url(r'^mint/(?P<minter_id>\d+)/(?P<qty>\d+)', arkapp_views.mint),
    url(r'^bind/(?P<key>\w+)/(?P<url>.+)', arkapp_views.bind),
    url(r'(P?<key>\w+)', arkapp_views.resolve)

]
