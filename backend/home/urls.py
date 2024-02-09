from django.urls import path
from home import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('search/', views.searchPage, name='search'),
]
