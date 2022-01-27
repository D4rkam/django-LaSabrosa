from django.shortcuts import render
from .models import Page

# Create your views here.
def other(request, page_id):
    page = {
        'page':Page.objects.get(id=page_id)
    }
    return render(request, "page/other.html", page)