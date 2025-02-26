
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('website-admin-portal/', admin.site.urls),
    path('', include('core.urls')),
]
