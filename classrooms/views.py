# from django.shortcuts import render

from rest_framework import generics
from .models import Classroom, Student, Attendance
from .serializers import ClassroomSerializer, StudentSerializer, AttendanceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ClassroomListCreate(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ... similar views for updating, deleting, etc.
