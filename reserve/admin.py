from django.contrib import admin
from .models import Hotel,Location,Review,Room,Customer,Reservation


admin.site.register(Review)
admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(Reservation)
