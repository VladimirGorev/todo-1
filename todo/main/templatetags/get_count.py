from django.template.defaulttags import register
from todo.settings import DIV_COUNT


@register.filter
def get_count(lists):
    """
    Возвращает список - количество, для генераци пустых блоков
    """
    return range(DIV_COUNT - len(lists))
