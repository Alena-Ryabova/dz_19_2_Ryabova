from django import template

register = template.Library()


@register.filter()
def text_limit(val):
    if len(val) > 100:
        return val[:100]
    else:
        return val
