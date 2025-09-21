from rest_framework import serializers
from school.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name',
            'surname',
            'last_name',
            'phone',
            'email',
            'date_of_birth',
            'price',
            'subject'
        ]

class ClassGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_group
        fields = [
            'id',
            'letter',
            'grade',
            'class_teacher',
            'room_number'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'teachers'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'id',
            'teacher',
            'order',
            'count',
            'discount'
        ]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'surname',
            'last_name',
            'date_of_birth',
            'address',
            'phone',
            'parent_name',
            'parent_middlename',
            'parent_phone',
            'class_group',
            'photo'
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'class_group',
            'subject',
            'teacher',
            'day_of_week',
            'start_time',
            'end_time',
            'room'
        ]

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = [
            'id',
            'student',
            'subject',
            'grade',
            'date_given',
            'semester'
        ]

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'id',
            'student',
            'schedule',
            'date',
            'status'
        ]

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = [
            'id',
            'subject',
            'class_group',
            'description',
            'assigned_date',
            'due_date'
        ]