from django.urls import path
from music import views

urlpatterns = [
    path('', views.songsPage, name='songs'),
    path('<slug>-ID-<pk>/', views.singleSongPage, name='single-song'),
]