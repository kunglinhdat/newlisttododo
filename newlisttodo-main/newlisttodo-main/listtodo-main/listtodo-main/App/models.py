from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES =[
        ('todo','ToDo'),
        ('working','Working'),
        ('done','Done')
    ]
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    comleted=models.BooleanField(default=False)
    status=models.CharField(max_length=16,choices=STATUS_CHOICES,default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='tasks',null=True,blank=True)

    def __str__(self):
        return self.description
