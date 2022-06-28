from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    class Meta:
        verbose_name='Student'