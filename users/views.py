from django.shortcuts import redirect, render
from .forms import RegistrUser,LoginUserForm, UserProfileForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register_user(request):
    """ Регистрация пользователя """
    if request.method == 'POST':
        form = RegistrUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.save()  
            login(request,user)  
            # messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('profile')  
    else:
        form = RegistrUser()
    return render(request, 'users/registration.html', {'form': form})

def login_user(request):
    """ Аутентификация пользователя """
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('profile')
        else:
            return messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = LoginUserForm()
    
    context = {
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'users/login.html', context)


@login_required
def profile(request):
    # Просто передаем request.user в контекст шаблона
    return render(request, 'users/profile.html', {
        'user': request.user
    })
# def profile(request):
#     return render(request, 'users/profile.html')


def logout_user(request):
    """ Выход с аккаунта """
    logout(request)
    return redirect('index')

