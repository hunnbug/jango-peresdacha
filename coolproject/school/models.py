from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

MAX_LENGTH_SHORT = 50
MAX_LENGTH_MEDIUM = 100
MAX_LENGTH_LONG = 255
MAX_LENGTH_ID = 20
MAX_LENGTH_PHONE = 11
MAX_LENGTH_CODE = 10
MAX_LENGTH_ROOM = 4


class Student(models.Model):
    student_id = models.CharField(max_length=MAX_LENGTH_ID, unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    surname = models.CharField(max_length=MAX_LENGTH_SHORT)
    date_of_birth = models.DateField()
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)
    parent_name = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True)
    parent_middlename = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True)
    parent_phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)


class Subject(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_MEDIUM)


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=MAX_LENGTH_ID, unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    last_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)
    email = models.EmailField(blank=True)
    subject = models.ForeignKey(Subject, related_name='teachers')


class Class(models.Model):
    CLASS_LEVELS = ['1 класс', '2 класс', '3 класс', '4 класс', '5 класс', 
                    '6 класс', '7 класс', '8 класс', '9 класс', '10 класс', '11 класс']
    
    name = models.CharField(max_length=MAX_LENGTH_CODE, unique=True)
    grade = models.CharField(max_length=9, choices=CLASS_LEVELS)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')
    room_number = models.CharField(max_length=MAX_LENGTH_ROOM, null=True)


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
    ]
    
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=MAX_LENGTH_ROOM)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_given = models.DateField(auto_now_add=True)
    semester = models.IntegerField(choices=[(1, '1 семестр'), (2, '2 семестр')])


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Присутствовал'),
        ('N', 'Отсутствовал'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homeworks')
    description = models.TextField()
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()