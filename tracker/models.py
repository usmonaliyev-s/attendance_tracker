from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.course_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='Attence status', default=False)

    def __str__(self):
        return f"{self.student.name} - {self.time} - {self.course} - {self.status}"