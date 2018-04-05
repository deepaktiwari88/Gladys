from django.db import models

# blueprint for database
class Restaurant(models.Model):          #generates primary key on its own
    rating = models.CharField(max_length=10)      #rating, name are all columns in database
    name = models.CharField(max_length=500)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)

    def __str__(self):          #string representation of the object
        return self.name + ' - ' + str(self.rating)
    
class Menu(models.Model):
    date = models.CharField(max_length=15)
    #dish_id = models.
    review = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

