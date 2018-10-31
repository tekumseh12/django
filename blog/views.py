from django.shortcuts import render

def snake(request):
    return render(request,"chest.html", {})
