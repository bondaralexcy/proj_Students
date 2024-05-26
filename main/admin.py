from django.contrib import admin
from main.models import Student


# admin.site.register(Student)
# В этом случае отображается информация из магического метода __str__


# Но для настройки отображения используется второй вариант:
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "is_active",
    )
    # А в этом случаае - названия заголовков берутся из verbose_name
    # models.CharField(max_length=100, verbose_name='имя')

    # Добавляем поля для фильтрации
    list_filter = ("is_active",)

    # Добавляем поля для поиска
    search_fields = (
        "first_name",
        "last_name",
    )
