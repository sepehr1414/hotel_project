from django.urls import path
from . import views


app_name = 'reserve'
urlpatterns = [
path('hotel_list/', views.ListHotel.as_view(), name='hotel-list'),
path('hotel/<int:pk>/', views.DetailHotel.as_view(), name='hotel-detail'),
path('reserve_form/',views.ReserveFormCreate.as_view(),name = 'reserve-form'),
path('reserve_detail/<int:pk>/', views.ReserveDetail.as_view(), name = 'reserve-detail'),
path('search/', views.filter_form, name='form-filter')
]
