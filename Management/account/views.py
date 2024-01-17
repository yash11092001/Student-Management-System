from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from Student.models import Details
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')

           

    return render(request,'account/login.html')

def register(request):
    if request.method=='POST':
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        un=request.POST.get('un')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c_password=request.POST.get('c_password')
        if password==c_password:
            if User.objects.filter(username=un).exists():
                messages.error(request,'usename alredy exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email alredy exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=fn,last_name=ln,username=un,email=email,password=password)
                    user.save()
                    return redirect('login')
        else:
            messages.error(request,'password does not match')
            return redirect('register')



    
    return render(request,'account/register.html')


@login_required(login_url='login')
def dashboard(request):
    students=Details.objects.all()
    context={
        'students':students
    }
    return render(request,'account/dashboard.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')


def student_details(request,id):
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

        data=Details.objects.get(pk=reg)
        data.name=name
        data.city=city
        data.clg_name=clg
        data.degree=degree
        data.passing_year=year
        data.percentage=percentage
        data.email=email
        data.mobile=mbl
        data.course=course
        data.fee_amount=amount
        data.save()
        return redirect('dashboard')
    
    student=Details.objects.get(pk=id)
    context={
        'student':student
    }
    return render(request,'account/studentdetails.html',context)

def delete(request,id):
    student=Details.objects.get(pk=id)
    student.delete()


    return redirect('dashboard')