from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager, PermissionsMixin)


class CustomUserManager(BaseUserManager):
    '''Custom user manager'''
    def create_user(self, email, password=None, **extra_fields):
        '''Creates and saves a user using email address'''
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''Creates and saves a new super user using email address'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that support using email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=32, unique=True)
    picture = models.ImageField(upload_to='ArtistsPictures/',
                                default='ArtistsPictures/default.jpg')
    slug = models.SlugField()
    bio = models.TextField(max_length=1024)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        if not self.username:
            self.username = 'user' + str(len(CustomUser.objects.all()))
        super().save(*args, **kwargs)


class Comment(models.Model):
    body = models.TextField(max_length=320)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
