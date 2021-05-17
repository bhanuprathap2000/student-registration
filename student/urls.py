from django.urls import path

from . import views
urlpatterns = [
    path('',views.show_students,name="showstudents"),
    path('/delete/<int:id>',views.delete_student,name='deletestudent'),
    path('/edit/<int:stu_id>',views.edit_student,name='editstudent'),
]
