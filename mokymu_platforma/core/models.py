from django.db import models
from datetime import timezone
from django.utils import timezone
import datetime

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=20)
    company_logo = models.ImageField()
    company_description = models.TextField()

class Course(models.Model):
    course_category = models.CharField(max_length=20)
    course_description = models.TextField()

class Courses_Company(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Student(models.Model):
    user_id = models.CharField(max_length=20)
    student_personalCode = models.CharField(max_length=20)
    registration_date = models.DateTimeField(default=datetime.datetime.now())
    delete_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

class CoursesGroup_Student(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

class Courses_Group(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    course_teacher_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

class User(models.Model):
    login_name = models.CharField(max_length=200)
    login_password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    photo = models.ImageField()
    user_created = models.TimeField (blank=False, null=False, default=datetime.datetime.now())
    other = models.CharField(max_length=200)

class Roles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_type = models.CharField(max_length=200)

class Company(models.Model):
    company_name = models.CharField(max_length=20)
    company_logo = models.ImageField()
    company_description = models.TextField()

class Course(models.Model):
    course_category = models.CharField(max_length=20)
    course_description = models.TextField()

class Courses_Company(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Student(models.Model):
    user_id = models.CharField(max_length=20)
    student_personalCode = models.CharField(max_length=20)
    registration_date = models.DateTimeField(default=datetime.datetime.now())
    delete_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

class CoursesGroup_Student(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

class Courses_Group(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    course_teacher_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)






class User(models.Model):
    login_name = models.CharField(max_length=200)
    login_password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    photo = models.ImageField()
    user_created = models.TimeField (blank=False, null=False, default=datetime.datetime.now())
    other = models.CharField(max_length=200)

class Roles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_type = models.CharField(max_length=200)