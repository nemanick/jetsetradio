from django.urls import path
from music import views

urlpatterns = [
    path('', views.songsPage, name='songs'),
    path('<slug>-ID-<pk>/', views.singleSongPage, name='single-song'),
    path('download/<int:track_id>/', views.download_track,
         name='download_track'),
]
