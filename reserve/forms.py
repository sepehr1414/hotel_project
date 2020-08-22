from django import forms
from django.forms import ModelForm
from .models import Reservation

class ReserveForm(ModelForm):
    model = Reservation
    fields = ['no_of_children', 'no_of_adult',
    'reservation_date_time','check_in_date_time',
    'check_out_date_time', 'customer', 'hotel_reserve', 'room_reserve']
