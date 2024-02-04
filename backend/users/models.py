from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from rest_framework.validators import ValidationError

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'

    ROLE_CHOICES = (
        (ADMIN, ADMIN),
        (USER, USER),
    )

    username = models.CharField(max_length=256, unique=True,)
    email = models.EmailField(unique=True,)
    password = models.CharField(max_length=16,)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default=USER,)
    veritificated = models.BooleanField(default=False,)
    bio = models.TextField(blank=True,)

    @property
    def is_stuff(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='subscriber')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='author')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='subscribe_unique'
            )
        ]

    def clean(self) -> None:
        if self.user == self.author:
            raise ValidationError('Нельзя оформить подписку на самого себя')

