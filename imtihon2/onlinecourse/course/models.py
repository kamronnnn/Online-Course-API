from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class Course(models.Model):
    """"Bu Class Kurs lar uchun"""
    name = models.CharField(max_length=100, help_text='Kurs Nomi')
    started = models.DateTimeField(help_text='Kurs Boshlanishi')
    duration = models.IntegerField(default=0, help_text='Kurs Davomiligi')
    description = models.TextField(null=True, blank=True, help_text='Kurs haqida')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text=' Bir Oylik Kurs Narxi')

    def __str__(self):
        return self.name


class CourseTheme(models.Model):
    """"Bu Class Kurs ni mavzulari, ya'ni kurs davomida qanaqa darslar bo'lishi"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Kurs Mavzusi')
    video = models.FileField(upload_to='theme/videos', validators=[
        FileExtensionValidator(allowed_extensions=['MP4', 'ASF', 'FLV', 'MKV', 'MOV'])
    ])
    description = models.TextField(null=True, blank=True, help_text='Mavzu haqida')

    def __str__(self):
        return self.name


class Comment(models.Model):
    """"Bu Class dars(mavzu) ga izoh qo'shish classi """
    coursetheme = models.ForeignKey(CourseTheme, on_delete=models.CASCADE)
    text = models.TextField(help_text='Izoh')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class CourseComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Like(models.Model):
    """"Bu Class dars(mavzu) ga yoqdi yoki yoqmadi uchun class"""
    coursetheme = models.ForeignKey(CourseTheme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likeordislike = models.BooleanField()








