from django.urls import path
from classes import views
from classes.models import UClass

urlpatterns = [
    path('', views.index, name ='index'),
    path('view/<id_uuid4>', views.view, name ='view'),
    path('addstudent/', views.addStudent, name = 'add-student')
]