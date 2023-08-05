# # models.py
# from django.db import models

# class Teacher(models.Model):
#     姓名 = models.CharField(max_length=255)
#     專長 = models.CharField(max_length=255)
#     聯絡方式 = models.CharField(max_length=255)
#     辦公室位置 = models.CharField(max_length=255)

# models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='123')
    # class Meta:
    #     db_table = 'fjuqapp_teacher' 
