from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    class Meta:
        verbose_name='Student'

####
# sudo apt-get install graphviz graphviz-dev
# pip3 install pygraphviz
# pip3 install django-extensions
#  python3 manage.py graph_models firstapp -g -o model_vi.png