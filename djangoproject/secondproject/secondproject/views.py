from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .form import usersForm

def homePage(request):
    data = {
        "title":"home page",
        "bdata":"I LOVE YOU",
        "clist":['java','python','css','html'],
        "student_details":[
            {'name':'prem kumar','phone':'9876543210'},
            {'name':'prem genius','phone':'9876543210'},
        ],
        "numbers":[10,20,304,90,506,70]

    }
    if request.method == "GET":
        output = request.GET.get('output')


    return render(request,"index.html",{'output':output})


def interview(request):
    return render(request,"interview.html")



def aboutUs(request):
    return HttpResponse("hello world")

def courses(request):
    return HttpResponse("hello courses")

def courseDetails(request,courseId):
    return HttpResponse(courseId)

def submitform(request):

    
    try:
        if request.method == "POST":

            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            res = n1+n2+n3
            data = {
                'n1':n1,
                'n2':n2,
                'res':res
            }
            
            return HttpResponse(data['n1'])
        
       
    except:
        pass
       
    
   



def formPage(request):
    c = ''
    fn  = usersForm()
    data = {'form':fn}

    try:
        if request.method == "POST":
            if request.POST.get('num1')=="":
                return render(request,"form.html",{'error':True})
            
            n = eval(request.POST.get('num1'))
            if n% 2 == 0:
                c = "Even Number"
            else:
                c = "Odd Number"

            data = {
                'form':fn,
                'c':c
            }
    except:
        pass
    return render(request,"form.html",data)
   

def formPage2(request):
    res = 0
    fn  = usersForm()
    data = {'form':fn}

    if request.method == "POST":
        if request.POST.get('num1')=="":
            return render(request,"form.html",{'error':True})
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST .get('num2'))
        res = n1+n2
        data = {
            'n1':n1,
            'n2':n2,
            'res':res,
            'form':fn
        }
       
        url = "/?output={}".format(res)
        # return HttpResponseRedirect(url)
        return redirect(url)
    except:
        pass
    
    return render(request,"form.html",data)


def calculator(request):
    return render(request,"calculator.html")
