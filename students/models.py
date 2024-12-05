from django.db import models

class Student(models.Model):
    student_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Student : {self.first_name} {self.last_name}"
