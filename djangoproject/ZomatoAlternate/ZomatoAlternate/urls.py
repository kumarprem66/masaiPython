"""ZomatoAlternate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dish import views as dviews
from dish.views import DishCreateView
from dish.views import DishListView,DishUpdateView,DishDeleteView,DishListViewShow
from dish.views import place_order,confirm_order,order_list,update_order_status,register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DishListViewShow.as_view(),name='dash_page'),
    path('menu/add/',DishCreateView.as_view(),name='add_dish'),
    path('menu/', DishListView.as_view(),name='menu_page'),
    path('dish/<int:pk>/delete/',DishDeleteView.as_view(),name='delete_dish'),
    path('dish/<int:pk>/update/',DishUpdateView.as_view(),name='update_dish'),
    path('confirmation',confirm_order,name='order_confirmation'),
    path('place_order/', place_order, name='place_order'),
    path('order_list/', order_list, name='order_list'),
    path('register/', register, name='register'),
    path('update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),
    path('login/', auth_views.LoginView.as_view(template_name='dish/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

