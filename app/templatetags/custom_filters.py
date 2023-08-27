from django import template

# Create a template Library instance
register = template.Library()

@register.filter(name='get_item')
def get_item(value, arg):
    return getattr(value, arg, '')
