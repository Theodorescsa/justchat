from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:index')
    context = {
        'form':form
    }
    return render(request,'authenticating/register.html',context)

def signin(request):
    next = request.GET.get('next')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.GET.get('next')
        is_auth = authenticate(request,username=username,password=password)
        if is_auth:
            login(request,is_auth)
            if next:
                return redirect(next)
            else:
                return redirect('chat:index')
    context = {}
    return render(request,'authenticating/signin.html',context)
def logout2(request):
    logout(request)
    return redirect('authenticating:signin')