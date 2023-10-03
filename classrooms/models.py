"""Data Containers
```
Classroom, Student, Attendance
```
"""
from django.db import models

class Classroom(models.Model):
    """Classroom Data Container"""
    name = models.CharField(max_length=255)

class Student(models.Model):
    """Student Data Container"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    studentID = models.CharField(max_length=50, unique=True)
    classrooms = models.ManyToManyField(Classroom, related_name='students')

class AttendanceStatus(models.TextChoices):
    """Enum for status of attendance.
    ```
    ABSENT, PRESENT, TARDY, HALF_DAY
    ```
    """
    ABSENT = 'Absent'
    PRESENT = 'Present'
    TARDY = 'Tardy'
    HALF_DAY = 'Half Day'

class Attendance(models.Model):
    """Attendance Data Container"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=AttendanceStatus.choices)

    class Meta:
        """Metadata for `Attendance`"""
        unique_together = ['student', 'classroom', 'date']
