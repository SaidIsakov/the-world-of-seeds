from django.shortcuts import redirect, render
from .forms import RegistrUser,LoginUserForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages


def register_user(request):
    """ Регистрация пользователя """
    if request.method == 'POST':
        form = RegistrUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.save()  
            login(request,user)  
            return redirect('profile')  
    else:
        form = RegistrUser()
    return render(request, 'users/registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('profile')
    else:
        form = LoginUserForm()
    
    context = {
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'users/login.html', context)


def profile(request):
    return render(request, 'users/user.html')

def logout_user(request):
    logout(request)
    return redirect('index')