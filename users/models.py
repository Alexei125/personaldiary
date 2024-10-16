from django.contrib.auth.models import AbstractUser
from django.db import models

from diary.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    is_active = models.BooleanField(
        default=False, **NULLABLE, verbose_name="Статус активности"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
