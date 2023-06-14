from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

import rooms.models
from accounts.forms import *


def authentication(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()  # Сохранение пользователя
            login(request, user)  # Авторизация пользователя
            messages.add_message(request, messages.SUCCESS,
                                 f"Здравствуйте, {user.name}! Вы успешно зарегистрировались.")
            return redirect('accounts:profile')
    else:
        registration_form = RegistrationForm()

    # Обработка отправки формы входа
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        user = login_form.authenticate_user()
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 f"Здравствуйте, {user.name}! Вы успешно вошли в аккаунт.")
            return redirect('core:home')  # Перенаправление на главную страницу после успешного входа

    return render(request, 'accounts/authentication.html', {
        'registration_form': registration_form,
        'login_form': login_form
    })


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         f"Успешный выход из аккаунта")
    return redirect('core:home')


def profile_view(request):
    booking_history = rooms.models.Booking.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html', {'booking_history': booking_history})
