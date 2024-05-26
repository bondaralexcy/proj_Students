# Пользовательский тег и фильтр

import datetime
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


# Создание тега, преобразующего текущую дату в заданный формат
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

# При создании фильтра вы можете столкнуться со следующими ситуациями:
# 1. Ваш фильтр не добавляет никаких не экранированных HTML-символов (<, >, ', " or &) в результат. В таком случае вы можете полностью положиться на политику автоматического экранирования Django. Для этого передайте параметр is_safe с значением True при регистрации функции фильтра:
#
# @register.filter(is_safe=True)
# def myfilter(value):
#     return value

# 2. Фильтр самостоятельно заботится об экранировании результата.
# Это необходимо если вы добавляете новый HTML в результат.
# В таком случае результат должен быть помечен как безопасный чтобы избежать последующего экранирования.
# Для этого используйте функцию django.utils.safestring.mark_safe().
# Но будьте осторожны. Необходимо не просто пометить результат как безопасный.
# Вы должны убедиться что результат действительно безопасен независимо от того, включено автоматическое экранирование или нет.
# Идея в том, чтобы фильтр правильно работал как при включенном автоматическом экранировании, так и выключенном.
# Для того, чтобы фильтр знал включено ли автоматическое экранирование, передайте параметр needs_autoescape со значением True
# при регистрации функций фильтра. (По умолчанию значение равно False).
# Этот параметр указывает Django что необходимо передать именованный аргумент autoescape при вызове функции фильтра,
# который равен True, если включено автоматическое экранирование, иначе False.
# Рекомендуем по умолчанию указать True в autoescape, чтобы при вызове функции в коде, экранирование было включено.



# Создание фильтра, который выделяет первый символ строки:
@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)