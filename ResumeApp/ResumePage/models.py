from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30, null=False, default="")
    email= models.EmailField(max_length=50, null=True, default="")
    message = models.CharField(max_length=400, null=True, default="")


    def __str__(self):
        return self.name
