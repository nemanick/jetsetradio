from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('', include('album.urls')),
    path('', include('artist.urls')),
    path('', include('genre.urls')),
    path('', include('music.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
