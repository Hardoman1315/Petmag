from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Главная страница
def vetmag_main(request):
    return render(request, 'main/vetmag_main.html')

# Каталог товаров
def vetmag_catalogue(request):
    return render(request, 'main/vetmag_catalogue.html')

# Страница авторизации
def vetmag_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # Получаем номер телефона из формы
        password = request.POST.get('password')  # Получаем пароль
        user = authenticate(request, username=phone_number, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('vetmag_personal_area')  # После успешной авторизации переходим в личный кабинет
        else:
            messages.error(request, "Неверный номер телефона или пароль.")
            return redirect('vetmag_login')
    return render(request, 'main/vetmag_login.html')

# Страница регистрации
def vetmag_registration(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        username = request.POST.get('username')
        
        # Проверка, что номер телефона не занят
        if User.objects.filter(username=phone_number).exists():
            messages.error(request, "Этот номер телефона уже используется.")
            return redirect('vetmag_registration')
        
        # Создаем нового пользователя
        user = User.objects.create_user(username=phone_number, password=password)
        user.first_name = username
        user.save()
        
        # Авторизуем пользователя
        login(request, user)
        return redirect('vetmag_personal_area')  # Перенаправляем на личную страницу
    
    return render(request, 'main/vetmag_registration.html')

# Личный кабинет пользователя
def vetmag_personal_area(request):
    if request.user.is_authenticated:
        # Передаем данные пользователя в шаблон
        user = request.user
        return render(request, 'main/vetmag_personal_area.html', {'user': user})
    else:
        return redirect('vetmag_login')

# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('vetmag_main')  # После выхода перенаправляем на главную страницу
    