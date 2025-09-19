from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Class)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Homework)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class StudentAdmin(admin.ModelAdmin):
    pass

