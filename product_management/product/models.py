from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Size(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class product(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
# This means every product belongs to one Django user.
    proid=models.IntegerField()
    name=models.CharField(max_length=50)

    image=models.ImageField(upload_to="product/",blank=True,null=True)

    color=models.CharField(max_length=100)
    size=models.ManyToManyField(Size)

    price = models.IntegerField()
    def __str__(self):
        return self.name  


# file=models.FileField(upload_to="files/")