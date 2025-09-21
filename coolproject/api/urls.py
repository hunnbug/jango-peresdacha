from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('teachers', TeacherViewSet, basename='teachers')
router.register('orders', OrderViewSet, basename='orders')
router.register('pos_orders', Pos_orderViewSet, basename='pos_orders')
router.register('class_groups', Class_groupViewSet, basename='class_groups')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('students', StudentViewSet, basename='students')
router.register('schedules', ScheduleViewSet, basename='schedules')
router.register('grades', GradeViewSet, basename='grades')
router.register('attendances', AttendanceViewSet, basename='attendances')
router.register('homeworks', HomeworkViewSet, basename='homeworks')
urlpatterns += router.urls