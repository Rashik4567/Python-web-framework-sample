from django.db import models

# Create your models here.
class products(models.Model):
    Name = models.CharField(max_length=265)
    Description = models.CharField(max_length=99999999999999)
    Price = models.IntegerField()
    Release_date = models.DateTimeField('Released on:')
    Color = models.CharField(max_length=1024)
    Picture_link = models.CharField(max_length=500)
    Stock = models.IntegerField()
    Offers = models.CharField(max_length=255)
    Company = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
