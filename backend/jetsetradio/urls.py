from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('artists/', include('artist.urls')),
    path('genre/', include('genre.urls')),
    path('songs/', include('music.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/reset_password.html'),
        name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/reset_password_sent.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/reset.html'), name=(
                 'password_reset_confirm')),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/reset_password_complete.html'), name=(
                 'password_reset_complete')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
