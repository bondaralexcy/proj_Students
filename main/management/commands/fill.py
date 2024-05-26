# Вызывать команду необходимо через всё тот же файл обслуживания фреймворка
# manage.py
# Сама команда должна обязательно наследоваться от базового класса и реализовывать обязательный метод:

# myapp/management/commands/fill.py
from django.core.management import BaseCommand
from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        # print('Hi, Sky!')

        student_list = [
            {"last_name": "Petrov", "first_name": "Ivan"},
            {"last_name": "Ivanov", "first_name": "Petr"},
            {"last_name": "Semenov", "first_name": "Aleksandr"},
            {"last_name": "Aleksandrov", "first_name": "Semen"},
        ]

        # Это способ для небольшого количества данных
        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        # Пакетное добавление
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        # print(students_for_create)
        Student.objects.bulk_create(students_for_create)
