from django import forms
from .models import Order, Dishes


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name','dish_items']