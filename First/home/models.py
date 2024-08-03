from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    number = models.CharField(max_length=125)
    date = models.DateField()

    def __str__(self):
        return self.name