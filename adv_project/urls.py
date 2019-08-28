from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]
