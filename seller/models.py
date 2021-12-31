from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class seller(models.Model):
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(max_length=7)
    deadline = models.DateTimeField(default= timezone.now())
    productimage = models.ImageField()

    def __str__(self):
        return self.productname
    
class bidding(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    productid = models.ForeignKey(seller,on_delete=models.CASCADE)
    bidamount = models.IntegerField(max_length=7)
