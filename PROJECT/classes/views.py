from django.shortcuts import render
import re
from django.contrib import messages
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from classes.models import UClass, UStudents
from django.views.generic import ListView
from django.db.models.functions import Now
from django.contrib.auth.models import User

def index(request):
    if request.method == "POST" and request.user.is_superuser:
        name = request.POST['name']
        price = request.POST['price']
        age = request.POST['age']
        time = request.POST['time']
        capacity = request.POST['capacity']
        nClass = UClass.objects.create(
            name = name,
            price = price,
            age = age,
            time = time,
            capacity = capacity,
            log_date = Now()
        )
        nClass.save()

    querysetUC=UClass.objects.order_by("-log_date").all()
    return render(request, "classes/index.html", {
        'classes_list': querysetUC.values,
        'date': datetime.now()
    })

def view(request, id_uuid4):
    cUsers = request.user
    if (request.user.is_authenticated and request.user.is_superuser):
        cUsers = User.objects.all()

    if request.method == "POST" and request.user.is_superuser:
        action = request.POST['action']
        id_c = request.POST['id']
        uClass = UClass.objects.get(id = id_c)
        if (action == 'update'):
            name = request.POST['name']
            price = request.POST['price']
            age = request.POST['age']
            time = request.POST['time']
            capacity = request.POST['capacity']
            teacher = request.POST['teacher']

            uClass.name = name
            uClass.price = price
            uClass.age = age
            uClass.time = time
            uClass.capacity = capacity
            uClass.log_date = Now()
            uClass.teacher = teacher
            uClass.save()
        elif (action == 'delete'):
            uClass.delete()
            return redirect('/classes')

    querysetUC=get_object_or_404(UClass, id=id_uuid4)
    querysetAUC=UClass.objects.order_by("-log_date").all()
    queryCStudents = UStudents.objects.filter(class_id=querysetUC.id).all()
    return render(
        request,
        'classes/index-view.html',
        {
            'users_list': cUsers,
            'class_view': querysetUC,
            'classes_list': querysetAUC,
            'students_list': queryCStudents,
            'name': id_uuid4,
            'date': datetime.now()
        }
    )

def addStudent(request):
    if (request.method == 'POST'):
        class_id = request.POST['class_id']
        g_name = request.POST['g_name']
        g_email = request.POST['g_email']
        c_name = request.POST['c_name']
        c_age = request.POST['c_age']
        message = request.POST['message']
        nStudent = UStudents.objects.create(
            class_id = class_id,
            g_name = g_name,
            g_email = g_email,
            c_name = c_name,
            c_age = c_age,
            message = message,
            log_date = Now()
        )
        nStudent.save()
        messages.info(request, f'Записахте успешно!')
    
    return redirect('/')