from django.db import models


# Create your models here.
class Dishes(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.dish_name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    status_choices = [
        ('received', 'Received'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='received')
    dish_items = models.ManyToManyField(Dishes)

    def __str__(self):
        return f"Order by {self.customer_name}"