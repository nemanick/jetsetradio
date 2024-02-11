from django.urls import path
from music import views

urlpatterns = [
    path('', views.songsPage, name='songs'),
    path('<slug>-ID-<pk>/', views.singleSongPage, name='single-song'),
    path('download/<int:track_id>/', views.downloadTrack,
         name='download-track'),
    path('create/', views.songCreateAndEdit, name='song-create'),
    path('edit/<slug>-ID-<pk>/', views.songCreateAndEdit, name='song-edit')
]
