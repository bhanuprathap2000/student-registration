from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm

from .models import Student
# Create your views here.
#show form which can add studnet data and also show saved studnet information.
def show_students(request):
    if request.method=='POST':
        student_form=StudentForm(request.POST)
        if student_form.is_valid():
            name=student_form.cleaned_data['name']
            rollnumber=student_form.cleaned_data['rollnumber']
            email=student_form.cleaned_data['email']
            year=student_form.cleaned_data['year']
            studentobj=Student(name=name,rollnumber=rollnumber,email=email,year=year)
            studentobj.save()
            student_form=StudentForm()
  
    else:
        student_form=StudentForm()
    studentdata=Student.objects.all()
    return render(request,'student/add_showstudents.html',{'form':student_form,'students':studentdata})

    #delete a specific record
def delete_student(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect('/')

def edit_student(request,stu_id):
    if request.method=='POST':
        student=Student.objects.get(pk=stu_id)
        updated_studentdata=StudentForm(request.POST,instance=student)

        if updated_studentdata.is_valid():
            updated_studentdata.save()
    else:
        student=Student.objects.get(pk=stu_id)
        updated_studentdata=StudentForm(instance=student)
        

    return render(request,'student/editstudent.html',{'form':updated_studentdata})



  