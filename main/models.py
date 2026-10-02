from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField(default=1)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"