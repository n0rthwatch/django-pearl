from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rooms.models import Room, Service, Staff, RoomImage


def home(request):
    rooms = Room.objects.all()
    services = Service.objects.all()
    staff = Staff.objects.filter(main=True)
    return render(request, 'core/home.html', {
        'rooms': rooms,
        'services': services,
        'staff': staff,
    })


def services(request):
    gallery = RoomImage.objects.all()
    services = Service.objects.all()
    staff = Staff.objects.all()
    return render(request, 'core/sevices.html', {
        'gallery': gallery,
        'services': services,
        'staff': staff,
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Отправка email
        try:
            send_mail(
                subject,
                f'Имя: {name}\nEmail: {email}\nТелефон: {phone}\nСообщение: {message}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )
        except BadHeaderError:
            messages.add_message(request, messages.ERROR,
                                 "Не удалось отправить сообщение. Перезагрузите страницу и попробуйте ещё раз")

        messages.add_message(request, messages.INFO, "Сообщение отправлено")
        return redirect('core:contact')
    return render(request, 'core/contact.html', {})
