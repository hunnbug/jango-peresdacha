from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path

urlpatterns = [
    path('info/', info_view),
    path('', info_view),
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teachers_detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teachers_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teachers_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teachers_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)