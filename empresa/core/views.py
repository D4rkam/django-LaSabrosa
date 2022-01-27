from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def visit(request):
    return render(request, "core/visit.html")

def history(request):
    return render(request, "core/history.html")