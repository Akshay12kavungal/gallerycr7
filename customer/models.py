from django.db import models
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=42)
    Email = models.EmailField()
    Password = models.CharField(max_length=42)
    Confirm_Password = models.CharField(max_length=42)


    def __str__(self):
        return self.Name


class uploadimage(models.Model):

    image=models.ImageField(upload_to='images')
    uploaded_at = models.DateTimeField(default=timezone.now)





