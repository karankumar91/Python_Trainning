from django.db import models

# Create your models here.
class student(models.Model):
    stu_id=models.IntegerField()
    stu_name=models.CharField(max_length=20)
    stu_branch=models.CharField(max_length=20)
    
    def __str__(self):
        return self.stu_name

        
