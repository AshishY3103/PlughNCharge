"""
URL configuration for CarOne project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ev_server.views import *
from CarDashboard.views import *
urlpatterns = [ 
               
    # path(" ", include('ev_server.url')),
    path("", find_ev_stations_view, name = 'dashev'),
    path('admin/', admin.site.urls),
    path('login/',user_login),
    path('TableSorted/',get_connectors),

    # path('map/',find_ev_stations_view)clear
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)