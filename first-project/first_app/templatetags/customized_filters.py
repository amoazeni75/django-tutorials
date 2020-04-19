from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This is a customized filter
    This cuts off all values of arg from the string
    :param value:
    :param arg:
    :return:
    """
    return value.replcae(arg, '')
