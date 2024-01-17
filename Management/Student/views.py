from django.shortcuts import render

from Student.models import Details
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'Student/home.html')

def record(request):
    return render(request,'Student/record.html')

def registration(request):
    if request.method=='POST':
        reg=request.POST.get('reg')
        name=request.POST.get('name')
        city=request.POST.get('city')
        clg=request.POST.get('clg')
        degree=request.POST.get('degree')
        year=request.POST.get('year')
        percentage=request.POST.get('percentage')
        email=request.POST.get('email')
        mbl=request.POST.get('mbl')
        course=request.POST.get('course')
        amount=request.POST.get('amount')
        


        student_obj=Details(reg_no=reg,name=name,city=city,clg_name=clg,degree=degree,passing_year=year,percentage=percentage,email=email,mobile=mbl,course=course,fee_amount=amount)
        student_obj.save()



    return render(request,'Student/registration.html')
@login_required(login_url='/account/login/')
def about_us(request):
    return render(request,'Student/about.html')

def java(request):
    return render(request,'Student/java.html')


def python(request):
    return render(request,'Student/python.html')


def aws(request):
    return render(request,'Student/aws.html')