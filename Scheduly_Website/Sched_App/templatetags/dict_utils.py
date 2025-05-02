# Sched_App/templatetags/dict_utils.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Given a dict and a key, return dict[key] if it exists, else return [].
    """
    if not dictionary:
        return []
    return dictionary.get(key, [])
