from django.db import models

NULLABLE = {"blank": True, "null": True}


class Record(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Запись", help_text="Введите запись"
    )
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите содержание записи"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания записи"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="records",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.title
