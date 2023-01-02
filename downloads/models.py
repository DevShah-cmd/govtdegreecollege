from django.db import models
from departments.models import Department
# Create your models here.


class Download(models.Model):
    title = models.CharField(max_length=220)
    link = models.URLField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return f"Download File Title : {self.title}"