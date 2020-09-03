from django.views.generic import ListView, DetailView, CreateView
from reserve.models import Hotel,Location,Reservation
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReserveForm
from django import forms
# Create your views here.


def home(request):
    return render(request,'index.html')

#creat a search view
class ListHotel(ListView):
    model = Hotel
    template_name = 'reserve/hotel_list.html'
    hotel_list = Hotel.objects.all()


class DetailHotel(DetailView):
    model = Hotel
    template_name='reserve/hotel_detail.html'


class ReserveFormCreate(CreateView):
    class_form = ReserveForm
    queryset = Reservation.objects.all()
    template_name = 'reserve/reservation_form.html'

    fields = ['no_of_children', 'no_of_adult','check_in_date_time',
    'check_out_date_time', 'customer', 'hotel_reserve', 'room_reserve']


    def form_valid(self, form):
        return super().form_valid(form)


class ReserveDetail(DetailView):
    template_name = 'reserve/reserve_detail.html'
    model = Reservation
    fields = ['no_of_children', 'no_of_adult',
    'reservation_date_time','check_in_date_time',
    'check_out_date_time', 'customer', 'hotel_reserve', 'room_reserve']


def is_valid_query(param):
    return param != '' and param is not None


def filter_form(request):
    hotel_qs = Hotel.objects.all()
    country_name_query = request.GET.get('country_name')
    city_name_query = request.GET.get('city_name')
    hotel_name_query = request.GET.get('hotel_name')
    grade_query = request.GET.get('grade-room')

    if is_valid_query(country_name_query):
        hotel_qs = hotel_qs.filter(location__country__icontains=country_name_query)
    if is_valid_query(city_name_query):
        hotel_qs = hotel_qs.filter(location__city__icontains=city_name_query)
    if is_valid_query(hotel_name_query):
        hotel_qs = hotel_qs.filter(name__icontains=hotel_name_query)

    context = {
        'queryset':hotel_qs
    }
    return render(request, 'search.html', context)
