from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
 
class Header(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Home Page Background Image : {self.image}"

    class Meta:
        verbose_name = 'Home Page Main Image'
        verbose_name_plural = 'Home Page Main Images'    
    



class Notice(models.Model):
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=20)
    notice = RichTextField()
    date_posted = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} | Date : {self.date_posted}"


class Event(models.Model):
    date = models.DateTimeField(default=datetime.now)    
    title = models.CharField(max_length=70)
    venue = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.title} | Venue : {self.venue} | Date : {self.date}"

class MeritList(models.Model):
    title = models.CharField(max_length=220)
    merit_list = RichTextField()

    def __str__(self):
        return f"{self.title}"



class Principal(models.Model):
    name = models.CharField(max_length = 120)
    message = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"Principal - {self.name}"
    
    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principal'   


class OurVision(models.Model):
    our_vision = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"Our Vision"
    
    class Meta:
        verbose_name = 'Our Vision'
        verbose_name_plural = 'Our Vision'   



class About(models.Model):
    image = models.ImageField()
    about = models.TextField()
    students = models.SmallIntegerField()
    faculty = models.SmallIntegerField()

    def __str__(self):
        return f"About Page Content | About, About Image, Total Students, Total Faculty"    




class Action(models.Model):
    image = models.ImageField()
    action = models.CharField(max_length= 50)
    link = models.URLField(max_length = 500)
    link_text = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.link_text} | {self.image} : Home Page Call to Action"


class OurValues(models.Model):
    heading = models.CharField(max_length = 50)
    value = models.CharField(max_length = 250)

    def __str__(self):
        return f"Our Value : {self.heading}"

    class Meta:
        verbose_name = 'Our Value'
        verbose_name_plural = 'Our Values'   


class Video(models.Model):
    heading = models.CharField(max_length = 250)
    link = models.URLField(max_length = 800)

    def __str__(self):
        return f"Video : {self.heading}"


class FormerPrincipal(models.Model):
    heading = models.CharField(max_length = 300)
    name = models.CharField(max_length = 220)
    image = models.ImageField()
    message = models.TextField()

    def __str__(self):
        return f"{self.heading} : {self.name}"


class CampusLife(models.Model):
    image = models.ImageField()
    heading = models.CharField(max_length = 220)
    about = RichTextField() 
    link = models.URLField(max_length = 800)

    def __str__(self):
        return f"{self.heading} : Campus Life "


class News(models.Model):
    type = models.CharField(max_length=80)
    title = models.CharField(max_length=200)
    published_date = models.DateField(auto_created=True, auto_now=True)
    content = RichTextField()

    def __str__(self):
        return f"News : {self.title} "

    class Meta:
        verbose_name = 'Featured News'
        verbose_name_plural = 'Featured News'   