from django.shortcuts import render
from . import models

# Create your views here.

def user_list(request):
    botlar=models.User.objects.all()
    return render(request, 'app/index.html', {'botlar': botlar})

def user_view(request, slug):
    botlar=models.User.objects.get(slag=slug)
    return render(request, 'app/user_view.html', {'botlar': botlar})
