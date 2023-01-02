from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=220, unique=True)
    image = models.ImageField()
    about = RichTextField()
    head_of_department_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Department : {self.name}"



class DepartmentHeader(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image : {self.image}"
    
    class Meta:
        verbose_name = 'Department Page Main Image'
        verbose_name_plural = 'Department Page Main Images'