from django.db import models
from django.core.validators import RegexValidator

# blueprint for database

# This table will store address of users and restaurant.


class Address(models.Model):

    house_no = models.IntegerField(null=True, blank=True)         # will be null for restaurant
    shop_no = models.IntegerField(null=True, blank=True)           # will be null for user
    sector = models.CharField(max_length=5)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    city = models.CharField(max_length=40)

    def isRestaurant(self):
        if self.house_no is None:
            return True
    def isUser(self):
        if self.shop_no is None:
            return True

    def __str__(self):
        return self.city + ' Sector: ' + self.sector


class Menu(models.Model):


    dishName = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, null=True)
    price = models.IntegerField()

# string representation of the object
    def __str__(self):
        return self.dishName + ' - ' + str(self.price)

class Restaurant(models.Model):          # generates primary key on its own


    rating = models.IntegerField()      # rating, name are all columns in database
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


# string representation of the object
    def __str__(self):
        return self.name + ' - ' + str(self.rating)


class Cuisine(models.Model):

    cuisineName = models.CharField(max_length=30)
    restaurantName = models.ManyToManyField(Restaurant)     # will return multiple restaurants having that cuisine



# a table for storing information about user
class User(models.Model):

    userName = models.CharField(max_length=30)      # should i make first name last name separate
    address = models.ForeignKey(Address, on_delete=models.CASCADE)      # address+contact of the user

# string representation of the object
    def __str__(self):
        return self.userName + ' - ' + str(self.address)

class Order(models.Model):

    orderDate = models.DateTimeField()
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)
    finalPrice = models.IntegerField()

    # calculates final price after some discounts

    def calcFinalPrice(self, discount):
        self.finalPrice = Menu.price - discount*Menu.price
        return self.finalPrice

# string representation of the object
    def __str__(self):
        return self.dish + ' - ' + str(self.finalPrice)

class DeliveryService(models.Model):

    deliveryGuyName = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    userDetails = models.ForeignKey(User, models.CASCADE)

class Chat(models.Model):

    username = models.CharField(max_length=25)
    message = models.TextField(max_length=200, null=True, blank=True)
    isuser = models.BooleanField()
