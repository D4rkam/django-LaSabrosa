from django import template
from page.models import Page

"""
Toda esta carpeta es un temple tag
En este caso se esta utilizando para modificar el template 'base.html'
"""
register = template.Library()

@register.simple_tag
def get_pages():
    pages = Page.objects.all()
    return pages