from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mokymu_platforma.core.models import Roles, Student, Course

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Roles, AuthorAdmin)
admin.site.register(Student, AuthorAdmin)
admin.site.register(Course, AuthorAdmin)