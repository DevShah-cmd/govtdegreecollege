from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.



class OnlineSection(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    content = RichTextField()
    url = models.URLField(null=True, blank=True)


    def __str__(self):
        return f"{self.title}"
