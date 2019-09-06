from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    sem_choices = (('I', '1'), ('II', '2'), ('III', 3), ('IV', 4),
    ('V', '5'), ('VI', '6'), ('VII', '7'), ('VIII', '8'))

    subject_code = models.CharField(primary_key = True, max_length = 100)
    subject_name = models.CharField(max_length = 100)
    ia_marks = models.IntegerField()
    exam_marks = models.IntegerField()
    total_no_lecture_hours = models.IntegerField()
    total_no_lecture_hours_per_week = models.IntegerField()
    exam_hours = models.IntegerField()
    credits = models.IntegerField()
    sem = models.CharField(max_length = 1, choices = sem_choices)


    def __str__(self):
        return self.subject_name



class Program(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Student(models.Model):

    user = models.OneToOneField(
    User, 
    default = None, 
    null = True, 
    on_delete=models.CASCADE
    )
    usn = models.CharField(primary_key = True, max_length=50)
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null = True)
    student_phone_no = models.CharField(max_length = 10)
    father_phone_no = models.CharField(max_length = 10)
    address = models.TextField()
    courses_taken = models.ManyToManyField(Course, related_name = 'students')
    program_taken = models.ForeignKey(Program, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.usn


class Sem(models.Model):
    sem_number = models.IntegerField()
    batch_year = models.IntegerField(primary_key=True)


