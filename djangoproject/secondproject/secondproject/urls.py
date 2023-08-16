"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from secondproject import views
from service import views as sviews
from news import views as nviews

urlpatterns = [
    path('',views.homePage),
    path('admin/', admin.site.urls),
    path('service/', sviews.checkModel),
    path('about/',views.aboutUs),
    path('courses/',views.courses),
    path('interview/',views.interview, name='interview'),
    path('submitform/',views.submitform, name='submitform'),
    path('calculate/',views.calculator, name='calculate'),
    # path('news/<newsid>',nviews.newsDetail),
    path('course/<slug:courseId>',views.courseDetails),
    path('form/',views.formPage),
    # not mention data type
    path('newsDetail/<newsid>',nviews.newsDetail),
    path('news/',nviews.news)

]
