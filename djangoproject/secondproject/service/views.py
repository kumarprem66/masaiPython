from django.shortcuts import render

# Create your views here.

from service.models import Service


def checkModel(request):
    serviceData  = Service.objects.all()
    # for i in serviceData:
    #     print(i.service_title)
    # print(serviceData)
    return render(request,'service.html',{'serviceData':serviceData})
