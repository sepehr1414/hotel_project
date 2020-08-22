from django.views.generic import ListView, DetailView, CreateView
from reserve.models import Hotel,Location,Reservation
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReserveForm

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

    fields = ['no_of_children', 'no_of_adult',
    'reservation_date_time','check_in_date_time',
    'check_out_date_time', 'customer', 'hotel_reserve', 'room_reserve']

    def form_valid(self, form):
        return super().form_valid(form)


class ReserveDetail(DetailView):
    template_name = 'reserve/reserve_detail.html'
    model = Reservation
    fields = ['no_of_children', 'no_of_adult',
    'reservation_date_time','check_in_date_time',
    'check_out_date_time', 'customer', 'hotel_reserve', 'room_reserve']
