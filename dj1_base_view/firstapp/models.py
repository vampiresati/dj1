from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    class Meta:
        verbose_name='Student'

from django.apps import apps
for app_config in apps.get_app_configs():
    l=app_config.name
    for model in app_config.get_models():
        n=model._meta.object_name
        print('apps',l,'models',n)
from firstapp.models import Parent
Parent._meta.get_fields()
