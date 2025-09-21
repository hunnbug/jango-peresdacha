"""
URL configuration for coolproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from school import views as school_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', school_views.info_view, name='info'),
    path('', school_views.info_view, name='info'),
    path('basket/', include('basket.urls')),

    path('teachers/', school_views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', school_views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', school_views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', school_views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', school_views.TeacherDeleteView.as_view(), name='teacher_delete'),

    path('subjects/', school_views.SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', school_views.SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/create/', school_views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/update/', school_views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', school_views.SubjectDeleteView.as_view(), name='subject_delete'),

    path('class_groups/', school_views.ClassGroupListView.as_view(), name='class_group_list'),
    path('class_group/<int:pk>/', school_views.ClassGroupDetailView.as_view(), name='class_group_detail'),
    path('class_group/create/', school_views.ClassGroupCreateView.as_view(), name='class_group_create'),
    path('class_group/<int:pk>/update/', school_views.ClassGroupUpdateView.as_view(), name='class_group_update'),
    path('class_group/<int:pk>/delete/', school_views.ClassGroupDeleteView.as_view(), name='class_group_delete'),

    path('students/', school_views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', school_views.StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', school_views.StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', school_views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', school_views.StudentDeleteView.as_view(), name='student_delete'),

    path('schedules/', school_views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/', school_views.ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedule/create/', school_views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/update/', school_views.ScheduleUpdateView.as_view(), name='schedule_update'),
    path('schedule/<int:pk>/delete/', school_views.ScheduleDeleteView.as_view(), name='schedule_delete'),

    path('grades/', school_views.GradeListView.as_view(), name='grade_list'),
    path('grade/<int:pk>/', school_views.GradeDetailView.as_view(), name='grade_detail'),
    path('grade/create/', school_views.GradeCreateView.as_view(), name='grade_create'),
    path('grade/<int:pk>/update/', school_views.GradeUpdateView.as_view(), name='grade_update'),
    path('grade/<int:pk>/delete/', school_views.GradeDeleteView.as_view(), name='grade_delete'),

    path('attendances/', school_views.AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/<int:pk>/', school_views.AttendanceDetailView.as_view(), name='attendance_detail'),
    path('attendance/create/', school_views.AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/<int:pk>/update/', school_views.AttendanceUpdateView.as_view(), name='attendance_update'),
    path('attendance/<int:pk>/delete/', school_views.AttendanceDeleteView.as_view(), name='attendance_delete'),

    path('homeworks/', school_views.HomeworkListView.as_view(), name='homework_list'),
    path('homework/<int:pk>/', school_views.HomeworkDetailView.as_view(), name='homework_detail'),
    path('homework/create/', school_views.HomeworkCreateView.as_view(), name='homework_create'),
    path('homework/<int:pk>/update/', school_views.HomeworkUpdateView.as_view(), name='homework_update'),
    path('homework/<int:pk>/delete/', school_views.HomeworkDeleteView.as_view(), name='homework_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)