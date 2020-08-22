from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm
from django.urls import reverse
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=11)
    email_address = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.customer_id} {self.last_name} {self.first_name}"


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(null=True)

    def __str__(self):
        return f"{self.country} {self.city}"


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    rooms_no = models.IntegerField()
    name = models.CharField(max_length=20)
    phone_no = models.BigIntegerField()
    grade = models.IntegerField()
    description = models.TextField(max_length=140, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(null = True , blank=True, upload_to = 'hotel_pics')

    class Meta:
        verbose_name_plural = 'Hotel'

    def __str__(self):
        return f"hotel name: {self.name} grade: {self.grade} country: {self.location.country}"


class Room(models.Model):
    GRADE_1 = "non vip"
    GRADE_2 = "vip"
    GRADE_CHOICES = (
        (GRADE_1, "non vip"),
        (GRADE_2, "vip"),
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    floor = models.IntegerField()
    number = models.IntegerField()
    capacity = models.IntegerField()
    grade = models.CharField(max_length=7, choices=GRADE_CHOICES)
    price = models.IntegerField()
    number_of_bed = models.SmallIntegerField(default=1)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="room_hotel", null=True)
    image_room = models.ImageField(null = True, blank = True, upload_to ='room_pics')

    
    def __str__(self):
        return f"hotel: {self.hotel.name}  grade: {self.grade} price:{self.price} number of bed: {self.number_of_bed}"


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    no_of_children = models.PositiveSmallIntegerField(default=0)
    no_of_adult = models.PositiveSmallIntegerField(default=1)
    reservation_date_time = models.DateTimeField(default=timezone.now)
    check_in_date_time = models.DateTimeField(default=timezone.now)
    check_out_date_time = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    hotel_reserve = models.ForeignKey(Hotel, on_delete=models.CASCADE ,null=True)
    room_reserve = models.ForeignKey(Room, on_delete=models.CASCADE ,null=True)

    def get_absolute_url(self):
        return reverse('hotel:reserve-detail', kwargs={'pk':self.reservation_id})


#add a review to user model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Review'

    def __str__(self):
        return self.comment


"""
class HotelManager(models.manager):
    def search(self,query=None):
        qs = request.get_query_set()
        if qs is not None:
            or_lookup = ( Q(name__icontains=query) &
                        Q(country__icontains=query)&
                        Q(check_in_date_time__icontains=query)&
                        Q(check_out_date_time__icontains=query)&
                        Q(no_of_adult__icontains=query)&
                        Q(no_of_children__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct()
        return qs
"""
