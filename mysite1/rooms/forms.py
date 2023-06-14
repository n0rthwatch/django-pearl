from django import forms
from django.utils import timezone
from rooms.models import Room, RoomImage
from .models import Booking


class RoomImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    slider_images = forms.ModelMultipleChoiceField(
        queryset=RoomImage.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
    )


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(
        label='Дата заезда',
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.localdate().strftime('%Y-%m-%d'), 'value': timezone.localdate().strftime('%Y-%m-%d')}),
        input_formats=['%Y-%m-%d'],
        required=True
    )
    check_out = forms.DateField(
        label='Дата выезда',
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.localdate().strftime('%Y-%m-%d'), 'value': timezone.localdate().strftime('%Y-%m-%d')}),
        input_formats=['%Y-%m-%d'],
        required=True
    )
    room_choice = forms.ModelChoiceField(
        queryset=Room.objects.all(),
        label='Номер',
        widget=forms.Select(attrs={'class': 'form-select', 'size': 6, 'onchange': "showRoomInfo(this)"}),
        required=True
    )
    adult_count = forms.IntegerField(
        label='Количество взрослых',
        widget=forms.NumberInput(attrs={'min': 1, 'max': 4}),
        required=True
    )
    child_count = forms.IntegerField(
        label='Количество детей',
        widget=forms.NumberInput(attrs={'min': 0, 'max': 4}),
        required=False
    )
    user_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False, help_text='Имя гостя установлено исходя из данных аккаунта пользователя'
    )
    user_email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'readonly': 'readonly'}),
        required=False,
        help_text='Email гостя установлено исходя из данных аккаунта пользователя'
    )
    guest_phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'placeholder': "8 (___) ___ __-__"}),
        required=True
    )

    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'user_name', 'user_email', 'adult_count', 'child_count']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Извлекаем request из kwargs
        super().__init__(*args, **kwargs)

        if request and request.user.is_authenticated:
            del self.fields['guest_name']
            del self.fields['guest_email']
            self.fields['user_name'].initial = request.user.name
            self.fields['user_email'].initial = request.user.email
        else:
            del self.fields['user_name']
            del self.fields['user_email']
