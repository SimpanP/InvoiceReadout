from django.db import models

# Create your models here.

class Invoice(models.Model):
    ocrNumber = models.CharField(max_length=13)
    bgNumber = models.CharField(max_length=20)
    price = models.FloatField()
    refNumber = models.CharField(max_length=20)
    isPaid = models.BooleanField()
    refrence = models.CharField(max_length=20)
    dueDate = models.DateField()

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')