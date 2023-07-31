from django.db import models

class Student(models.Model):
    regno=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    def __str__(self):
        return self.regno
