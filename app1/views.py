from django.shortcuts import render
from . import models

# Create your views here.

def rendering(request):
    # users=[
    #     {'ism':'Azizbek','familiya':'Abdurahimov','yosh':15},
    #     {'ism':'Shaxzod','familiya':'Zuparov','yosh':16},
    #     {'ism':'Doston','familiya':'Mirakilov','yosh':12}
    # ]
    users= models.User.objects.all()
    return render(request,'app/index.html',context={"botlar":users})    