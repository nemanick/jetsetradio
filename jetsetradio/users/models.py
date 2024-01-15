from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    ADMIN ='admin'
    USER='user'

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
    

class Follow(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriber')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_follow'
            )
        ]


class UserOptions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='')
    background_color = models.CharField(max_length=7, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[0-9a-fA-F]+$',
            message='Введите допустимый hex-код',
            code='invalid_hex_code',
        )
    ])
    text_color = models.CharField(max_length=7, null=True, blank=True, 
                                                     validators=[
                                                        RegexValidator(
                                                            regex='^[0-9a-fA-F]+$',
                                                            message='Введите допустимый hex-код',
                                                            code='invalid_hex_code',)])
