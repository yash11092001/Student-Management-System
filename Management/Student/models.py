from datetime import datetime
from django.db import models

# Create your models here.
class Details(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    clg_name=models.CharField(max_length=255)
    degree=models.CharField(max_length=255)
    passing_year=models.IntegerField()
    percentage=models.FloatField()
    email=models.EmailField()
    mobile=models.CharField(max_length=255)
    course=models.CharField(max_length=255,null=True)
    fee_amount=models.IntegerField()
    
    ad_date=models.DateField(default=datetime.now)
    def __str__(self):
        return self.name

                    