from django.urls import path
from artist import views

urlpatterns = [
    path('', views.artistsPage, name='artists'),
    path('<slug>-ID-<pk>/', views.signleArtistPage,
         name='single-artist'),
    path('<slug>-ID-<pk>/edit/', views.singleArtistEdit,
         name='single-artist-edit'),
]
