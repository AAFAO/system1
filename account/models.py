from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime

# from django.contrib.auth import get_user_model
# User = get_user_model()


Dep_list = (
    ('lib', 'Library'),
    ('Reg', 'registeration'),
    ('Free', 'Free_Dep'),
    ('Finance', 'Finance'),
    ('T&D', 'training and development'),
    ('Dep_Head', 'Department Head')
    )

St_Stage = (
    ('First', 'First'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Forth', 'Forth')
    )

St_dep=(
    ('Net', 'Network'),
    ('Soft', 'Software')
    )

class department(models.Model):
    Dep_name=models.CharField(max_length=255,choices=Dep_list,null=True)
    checked = models.BooleanField(default=False)
    def str(self):
        return self.Dep_name


class User(AbstractUser):
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    def str(self):
        return self.username


class req(models.Model):
    dep=models.ForeignKey(department,on_delete=models.CASCADE)
    st_name=models.CharField(max_length=255)
    Stage=models.CharField(max_length=300 , choices=St_Stage , blank=True)
    student_dep=models.CharField(max_length=300 , choices=St_dep ,blank=True)
    checked = models.BooleanField(default=False)
    Email=models.EmailField()
    phone_num=models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    
    def str(self):
        return self.st_name