from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import *
from .forms import *

def info_view(request):
    return render(request, 'info.html')

class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects_list.html'
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects_detail.html'
    context_object_name = 'subjects'

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subjects_delete.html'
    context_object_name = 'subjects'
    success_url = reverse_lazy('subject_list')

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects_create.html'
    context_object_name = 'subjects'
    success_url = reverse_lazy('subject_list')
    fields = ['name']

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subjects_update.html'
    context_object_name = 'subjects'
    success_url = reverse_lazy('subject_list')
    fields = ['name']

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers_detail.html'
    context_object_name = 'teacher'

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers_create.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers_update.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')

# Class_group Views
class ClassGroupListView(ListView):
    model = Class_group
    template_name = 'class_groups_list.html'
    context_object_name = 'class_groups'

class ClassGroupDetailView(DetailView):
    model = Class_group
    template_name = 'class_groups_detail.html'
    context_object_name = 'class_group'

class ClassGroupDeleteView(DeleteView):
    model = Class_group
    template_name = 'class_groups_delete.html'
    context_object_name = 'class_group'
    success_url = reverse_lazy('class_group_list')

class ClassGroupCreateView(CreateView):
    model = Class_group
    form_class = ClassGroupForm
    template_name = 'class_groups_create.html'
    context_object_name = 'class_group'
    success_url = reverse_lazy('class_group_list')

class ClassGroupUpdateView(UpdateView):
    model = Class_group
    form_class = ClassGroupForm
    template_name = 'class_groups_update.html'
    context_object_name = 'class_group'
    success_url = reverse_lazy('class_group_list')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students_detail.html'
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students_create.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students_update.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')

# Schedule Views
class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedules_list.html'
    context_object_name = 'schedules'

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedules_detail.html'
    context_object_name = 'schedule'

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedules_delete.html'
    context_object_name = 'schedule'
    success_url = reverse_lazy('schedule_list')

class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedules_create.html'
    context_object_name = 'schedule'
    success_url = reverse_lazy('schedule_list')

class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedules_update.html'
    context_object_name = 'schedule'
    success_url = reverse_lazy('schedule_list')

# Grade Views
class GradeListView(ListView):
    model = Grade
    template_name = 'grades_list.html'
    context_object_name = 'grades'

class GradeDetailView(DetailView):
    model = Grade
    template_name = 'grades_detail.html'
    context_object_name = 'grade'

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades_delete.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('grade_list')

class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grades_create.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('grade_list')

class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grades_update.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('grade_list')

# Attendance Views
class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendances_list.html'
    context_object_name = 'attendances'

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendances_detail.html'
    context_object_name = 'attendance'

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'attendances_delete.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance_list')

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendances_create.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance_list')

class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendances_update.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance_list')

# Homework Views
class HomeworkListView(ListView):
    model = Homework
    template_name = 'homeworks_list.html'
    context_object_name = 'homeworks'

class HomeworkDetailView(DetailView):
    model = Homework
    template_name = 'homeworks_detail.html'
    context_object_name = 'homework'

class HomeworkDeleteView(DeleteView):
    model = Homework
    template_name = 'homeworks_delete.html'
    context_object_name = 'homework'
    success_url = reverse_lazy('homework_list')

class HomeworkCreateView(CreateView):
    model = Homework
    form_class = HomeworkForm
    template_name = 'homeworks_create.html'
    context_object_name = 'homework'
    success_url = reverse_lazy('homework_list')

class HomeworkUpdateView(UpdateView):
    model = Homework
    form_class = HomeworkForm
    template_name = 'homeworks_update.html'
    context_object_name = 'homework'
    success_url = reverse_lazy('homework_list')