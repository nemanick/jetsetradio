from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include()),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
