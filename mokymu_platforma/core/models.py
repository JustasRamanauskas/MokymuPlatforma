from django.db import models
import datetime
from django.contrib.auth.models import User, UserManager


# Create your models here.

class Roles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_type = models.CharField(max_length=200)


class Company(models.Model):
    roles_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField()
    company_description = models.TextField()


class Course(models.Model):
    course_category = models.CharField(max_length=200)
    course_description = models.TextField()


class CoursesCompany(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Student(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    student_personalCode = models.CharField(max_length=200)
    registration_date = models.DateTimeField(default=datetime.datetime.now())
    delete_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)


class Teacher(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    other_info = models.CharField(max_length=200)


class Pricing(models.Model):
    course_id = models.CharField(max_length=200)
    discount = models.IntegerField()
    from_date = models.DateTimeField(blank=True, null=True)
    till_date = models.DateTimeField(blank=True, null=True)
    course_regular_price = models.IntegerField()


class CoursesGroup(models.Model):
    course_company_id = models.ForeignKey(CoursesCompany, on_delete=models.DO_NOTHING)
    course_teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    course_group_description = models.TextField()
    course_group_price = models.IntegerField()
    course_pricing_id = models.ForeignKey(Pricing, on_delete=models.DO_NOTHING)


class Client(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=200)
    company_code = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)


class ScheduleCourse(models.Model):
    course_group_id = models.ForeignKey(CoursesGroup, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(blank=True, null=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    start_theory_date = models.DateTimeField(blank=True, null=True)
    finish_theory_date = models.DateTimeField(blank=True, null=True)
    start_practice_date = models.DateTimeField(blank=True, null=True)
    finish_practice_date = models.DateTimeField(blank=True, null=True)
    exam_date = models.DateTimeField(blank=True, null=True)


class ContractStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    schedule_course_id = models.ForeignKey(ScheduleCourse, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    payment_method = models.CharField(max_length=200)
    payment_delay = models.IntegerField


class StudentFinishedCourses(models.Model):
    schedule_course_id = models.ForeignKey(ScheduleCourse, on_delete=models.DO_NOTHING)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    finish_date = models.DateTimeField(blank=True, null=True)
    valid_until_date = models.DateTimeField(blank=True, null=True)
    theory_result = models.IntegerField()
    practical_result = models.ImageField()


class CoursesGroupStudent(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)


