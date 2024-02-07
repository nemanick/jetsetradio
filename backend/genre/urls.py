from django.urls import path
from genre import views


urlpatterns = [
    path('<slug>-ID-<pk>/', views.GenrePage, name='genre')
]
