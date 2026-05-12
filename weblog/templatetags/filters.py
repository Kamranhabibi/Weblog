import datetime
from django.template import Library

register = Library()


@register.filter
def cutter(value,arg):
    return value[:arg]


@register.simple_tag
def current(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag("weblog/include/result.html")
def show_result(query):
    return {"text":query}