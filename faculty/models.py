from django.db import models
from ckeditor.fields import RichTextField

from departments.models import Department
# Create your models here.


class Staff(models.Model):
    number_in_order = models.SmallIntegerField(unique=True)
    image = models.ImageField()
    name = models.CharField(max_length=220)
    designation = models.CharField(max_length=220)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null= True, blank= True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    location = models.CharField(max_length=220, null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    honors_awards = models.TextField(null=True, blank=True)
    publications = models.TextField(null=True, blank=True)
    head_of_department = models.BooleanField(null=True, blank=True, default=False)
    about = RichTextField()

    def __str__(self):
        return f"{self.number_in_order} | Name : {self.name} | Designation : {self.designation} "




class StaffHeader(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image : {self.image}"

    class Meta:
        verbose_name = 'Staff Page Main Image'
        verbose_name_plural = 'Staff Page Main Images'