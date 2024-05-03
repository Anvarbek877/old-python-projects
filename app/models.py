from django.db import models

# Create your models here.
class Movie(models.Model):
    image=models.ImageField(upload_to="images/")
    name=models.CharField(max_length=50)
    time=models.CharField(max_length=20)
    release=models.DateField()
    vedioadjactive=models.CharField(max_length=10)
    syujeti=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    title=models.TextField()
    country=models.CharField(max_length=40)
    vedio=models.FileField(upload_to="film/")
    baholash=models.IntegerField()


