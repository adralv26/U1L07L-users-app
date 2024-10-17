from django.shortcuts import render
# Create your views here.
def userspage(request):
        context = {
        'active_link': 'users'
    }
        return render(request,'registers.html',context)