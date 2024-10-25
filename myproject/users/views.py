from django.shortcuts import render, redirect
# from django.contrib.auth.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.
def userspage(request):
        # check if form is submitted
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("posts:list")
        else:
            form = CustomUserCreationForm()
        context = {
        'active_link': 'register',
        'form':form,
    }
        return render(request,'users/registers.html',context)