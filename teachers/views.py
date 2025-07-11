from django.db.models import Count
from django.db.models.functions import NullIf
from django.shortcuts import render, redirect
from django.db.models import ExpressionWrapper, FloatField, F, Count, Q

from courses.models import Course
from students.models import Student
from teachers.models import Teacher

# Create your views here.
def teachers_list(request):
    teachers = Teacher.objects.annotate(
    num_students=Count('course__student', distinct=True),
    num_courses=Count("course", distinct=True)
    )
    data = {
        "teachers": teachers,
    }
    return render(request, "teachers/teachers_list.html", data)

def add_teacher(request):
    if request.method == "POST":
        Teacher.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone_number=request.POST.get('phone_number'),
        )
        return redirect('/teacher/list/')

    return render(request, "teachers/add_teacher.html")


def edit_teacher(request, id):
    if request.method == "POST":
        teacher = Teacher.objects.get(pk=id)
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.phone_number = request.POST.get('phone_number')
        teacher.save()
        return redirect('/teacher/list/')
    teacher = Teacher.objects.get(id=id)
    data = {
        "teacher": teacher,
    }
    return render(request, "teachers/edit_teacher.html", data)

def delete_confirmation_teacher(request, id):
    teacher = Teacher.objects.get(pk=id)
    data = {
        "teacher": teacher,
    }
    return render(request, "teachers/delete_confirmation_teacher.html", data)

def delete_teacher(request, id):
    Teacher.objects.get(pk=id).delete()
    return redirect('/teacher/list/')

def teacher_details(request, id):
    teacher = Teacher.objects.get(pk=id)
    courses = Course.objects.filter(course_teacher=teacher)
    students = Student.objects.annotate(
        total=Count('attendance'),
        present=Count('attendance', filter=Q(attendance__status=True)),
    ).annotate(
        attendance_rate=ExpressionWrapper(
            100.0 * F('present') / NullIf(F('total'), 0),
            output_field=FloatField()
        )
    ).filter(course__course_teacher=teacher)
    data = {
        "teacher": teacher,
        "courses": courses,
        "students": students,
    }
    return render(request, "teachers/teacher_details.html", data)
