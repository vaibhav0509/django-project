from django import template

register = template.Library()


def get_index(value,index):
    return value[int(index)]

def get_dict_value(dict,key):
    return dict[key]

register.filter('get_index',get_index)
register.filter('get_dict_value',get_dict_value)