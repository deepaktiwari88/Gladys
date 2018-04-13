from django.contrib import admin
from .models import Address, Menu, Restaurant, Cuisine, User, Order, DeliveryService, Chat
# Register your models here.

admin.site.register(Address)
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Cuisine)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(DeliveryService)
admin.site.register(Chat)
