from django.shortcuts import render, redirect,get_object_or_404
from . import models
from . import forms

def user_list(request):
    botlar = models.User.objects.all()
    return render(request, 'app/index.html', {'botlar': botlar})

def user_view(request, slug):
    botlar = models.User.objects.get(slug=slug)
    return render(request, 'app/user_view.html', {'botlar': botlar})
def user_create(request):
    if request.POST:
        form=forms.userForm(request.POST,request.FILES)
        if form.is_valid():
             form.save()
        return redirect('user_list')
    else:
        form = forms.userForm()
    return render(request, 'app/user_create.html',{'form':form})

def user_update(request, slug):
    user = get_object_or_404(models.User, slug=slug)

    if request.method == "POST":
        user.ism = request.POST.get('name')
        user.familiya = request.POST.get('surename')
        user.yosh = request.POST.get('age')

        if request.FILES.get('picture'):
            user.picture = request.FILES.get('picture')

        user.save()
        return redirect('user_detail', slug=user.slug)

    return render(request, 'app/user_update.html', {'user': user})

def user_delete(request,slug):
    users = get_object_or_404(models.User, slug=slug)
    if request.POST:
        users.delete()
        return redirect('user_list')
    return render(request, 'app/user_delete.html', {'botlar': users})

