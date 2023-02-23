from django.shortcuts import render

# Made by me
def index(request):
    return render(request, 'index.html')