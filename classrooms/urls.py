from django.urls import path
from .views import ClassroomListCreate, StudentListCreate, AttendanceListCreate

urlpatterns = [
    path('classrooms/', ClassroomListCreate.as_view(), name='classroom-list-create'),
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('attendances/', AttendanceListCreate.as_view(), name='attendance-list-create'),
    # ... URLs for updating, deleting, etc.
]
