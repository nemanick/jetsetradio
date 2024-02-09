from django.urls import path
from album import views

urlpatterns = [
    path('', views.AlbumsPage, name='albums'),
    path('<slug>-ID-<pk>/', views.SingleAlbumPage, name='single-album')
]