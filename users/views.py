from django.shortcuts import redirect, render
from .forms import RegistrUser,LoginUserForm, CustomUserUpdateForm
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
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return redirect('profile')
    # Просто передаем request.user в контекст шаблона
    else:
        form = CustomUserUpdateForm(instance=request.user) # GET-запрос - создаём форму с данными пользователя
        
    return render(request, 'users/profile.html', {
        'title': 'Профиль',
        'user': request.user,
        'form':form,
    })




def logout_user(request):
    """ Выход с аккаунта """
    logout(request)
    return redirect('index')