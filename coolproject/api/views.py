from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from school.models import *
from .permission import *

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [CustomPermissions]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class Pos_orderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class Class_groupViewSet(viewsets.ModelViewSet):
    queryset = Class_group.objects.all()
    serializer_class = ClassGroupSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage