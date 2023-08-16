from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Dishes
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

def mainPage(request):
    return render(request,'dish/index.html')


class DishCreateView(CreateView):
    model = Dishes
    fields = ['dish_name','price']
    success_url = reverse_lazy('menu_page')

class DishListView(ListView):
    model = Dishes
    template_name = 'dish/menu.html'  # Replace with the actual template name
    context_object_name = 'dishes'  # The variable name to use in the template




class DishListViewShow(ListView):
    model = Dishes
    template_name = 'dish/dashboard.html'  # Replace with the actual template name
    context_object_name = 'dishes'  # The variable name to use in the template


class DishUpdateView(UpdateView):
    model = Dishes
    fields = ['dish_name','price']
    template_name = 'dish/update_dish.html'
    success_url = reverse_lazy('menu_page')


class DishDeleteView(DeleteView):
    model = Dishes
    template_name = "dish/delete_dish.html"
    success_url = reverse_lazy('menu_page')
    context_object_name = 'dish' 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

def confirm_order(request):
    return render(request,"dish/confirmation.html")



@login_required(login_url='login')
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Check dish availability
            selected_dishes = form.cleaned_data['dish_items']

            # create order object
            order = Order(customer_name=form.cleaned_data['customer_name'])
            order.save()
            for dish in selected_dishes:
                order.dish_items.add(dish)
                # dish.is_available = False  # Update dish availability
                dish.save()
            
            return redirect('order_confirmation')
            # for dish in selected_dishes:
            #     if not dish.is_available:  # Add a field 'is_available' to your Dish model
            #         # Handle unavailability (e.g., show an error message)
            #         return render(request, 'dish/place_order.html', {'form': form, 'error_message': f"{dish} is not available"})
            
            # form.save()
            # return redirect('order_confirmation')  # Redirect to a confirmation page
    else:
        form = OrderForm()


    return render(request,'dish/place_order.html',{'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'dish/order_list.html', {'orders': orders})



# def update_order_status(request, order_id):
#     order = Order.objects.get(pk=order_id)

#     if request.method == 'POST':
#         new_status = request.POST.get('new_status')
#         order.status = new_status
#         order.save()
#         return redirect('order_list')  # Redirect to the orders list

#     return render(request, 'dish/update_order.html', {'order': order})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Order

def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        
        if new_status == 'completed':
            # Delete the order if the new status is 'completed'
            order.delete()
        else:
            # Update the order status
            order.status = new_status
            order.save()

        return redirect('order_list')  # Redirect to the orders list

    return render(request, 'dish/update_order.html', {'order': order})
   




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dash_page')
    else:
        form = UserCreationForm()
    return render(request, 'dish/register.html', {'form': form})



# def my_view(request):
#     context = {
#         'user': request.user  # Include the 'user' variable in the context
#     }
#     return render(request, 'dish/login.html', context)








