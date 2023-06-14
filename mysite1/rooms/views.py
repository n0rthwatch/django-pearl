from django.conf import settings
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import DetailView, ListView

from .forms import BookingForm
from .models import Room, Category
from datetime import datetime


def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request=request)

        if form.is_valid():
            booking = form.save(commit=False)
            room = form.cleaned_data['room_choice']
            booking.room = room

            if request.user.is_authenticated:
                booking.user = request.user
                booking.guest_name = request.user.name
                booking.guest_email = request.user.email
            else:
                booking.guest_name = form.cleaned_data['guest_name']
                booking.guest_email = form.cleaned_data['guest_email']

            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            nights_count = (check_out - check_in).days + 1
            booking.price = room.price * nights_count

            room.is_available = False
            room.check_in = check_in
            room.check_out = check_out
            room.booked_by = request.user if request.user.is_authenticated else None
            room.save()

            booking.check_in = check_in
            booking.check_out = check_out

            if not booking.child_count:
                booking.child_count = False
            booking.save()

            html_message = render_to_string('core/email_booking_template.html', {
                'booking': booking
            })

            # Создание экземпляра EmailMultiAlternatives
            subject = f'Гостиничный комплекс "Жемчуг" | Бронирование номера на {check_in.strftime("%d.%m.%Y")}'
            text_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject, text_message, settings.EMAIL_HOST_USER, [booking.guest_email])

            # Добавление HTML-версии письма
            email.attach_alternative(html_message, "text/html")

            try:
                email.send()
            except BadHeaderError:
                messages.add_message(request, messages.ERROR,
                                     "Не удалось отправить сообщение. Перезагрузите страницу и попробуйте ещё раз")

            messages.add_message(request, messages.SUCCESS,
                                 f"Номер '{room.title}' забронирован на {check_in.strftime('%d.%m.%Y')}\n Сообщение с подробными данными бронирования было отправлено на Email {booking.guest_email}")
            return redirect('core:home')
    else:
        form = BookingForm(request=request)

    return render(request, 'rooms/book_room.html', {'form': form})


def booking_success(request):
    return render(request, 'rooms/booking_success.html')


def room_info(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    check_in = ''
    check_out = ''

    if room.check_out:
        check_out = room.check_out.strftime('%d.%m.%Y')

    if room.check_in:
        check_in = room.check_in.strftime('%d.%m.%Y'),

    data = {
        'name': room.title,
        'description': room.short_description,
        'image_url': room.main_image.url,
        'max_adults': room.max_adults,
        'max_children': room.max_children,
        'services': list(room.services.values()),  # Преобразование ManyRelatedManager в список
        'availability': room.is_available,
        'check_in': check_in,
        'check_out': check_out,
        'price': intcomma(room.price),
        'slug': room.slug
    }

    return JsonResponse(data)


def check_availability(request):
    availability = True

    room_id = request.GET.get('room_id')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')

    check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
    check_out = datetime.strptime(check_out, '%Y-%m-%d').date()

    room = get_object_or_404(Room, pk=room_id)
    nights_count = (check_out - check_in).days + 1
    price = room.price * nights_count

    room_check_in = room.check_in
    room_check_out = room.check_out

    if room_check_in and room_check_out:
        if (check_in < room_check_in and check_out <= room_check_in) or (check_in >= room_check_out and check_out > room_check_out):
            availability = True
        else:
            availability = False

    data = {
        'availability': availability,
        'room_check_in': room_check_in.strftime('%d.%m.%Y'),
        'room_check_out': room_check_out.strftime('%d.%m.%Y'),
        'price': intcomma(price),
        'nights_count': nights_count
    }

    return JsonResponse(data)


class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'
    slug_url_kwarg = 'room_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.annotate(num_rooms=Count('room'))
        context['categories'] = categories
        context['count_rooms'] = Room.objects.count()
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')  # Получаем параметр фильтрации по категории из URL
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_with_counts = Category.objects.annotate(num_rooms=Count('room'))
        context['categories_with_counts'] = categories_with_counts
        return context
