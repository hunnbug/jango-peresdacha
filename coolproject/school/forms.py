from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'teacher_id', 'first_name', 'surname', 'last_name', 
            'date_of_birth', 'phone', 'email', 'subject', 'photo'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': '79991234567'}),
        }

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = Class_group
        fields = ['letter', 'grade', 'class_teacher', 'room_number']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id', 'first_name', 'surname', 'last_name', 
            'date_of_birth', 'address', 'phone', 'parent_name', 
            'parent_middlename', 'parent_phone', 'class_group', 'photo'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'phone': forms.TextInput(attrs={'placeholder': '79991234567'}),
            'parent_phone': forms.TextInput(attrs={'placeholder': '79991234567'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'class_group', 'subject', 'teacher', 
            'day_of_week', 'start_time', 'end_time', 'room'
        ]
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade', 'semester']
        widgets = {
            'grade': forms.NumberInput(attrs={'step': '0.1', 'min': '1', 'max': '5'}),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'schedule', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'class_group', 'description', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }