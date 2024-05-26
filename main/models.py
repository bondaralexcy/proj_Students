from django.db import models

NULLABLE = {"null": True, "blank": True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="имя")
    last_name = models.CharField(max_length=100, verbose_name="фамилия")
    # avatar = models.ImageField(upload_to='students/',verbose_name='аватар',null=True, blank=True)
    avatar = models.ImageField(upload_to="students/", verbose_name="аватар", **NULLABLE)

    # добавляем поле в модель и тут же создаем миграцию: >python3 manage.py makemigrations и перименяем ее
    is_active = models.BooleanField(default=True, verbose_name="учится")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"
        ordering = ("last_name",)
