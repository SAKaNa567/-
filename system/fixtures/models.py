from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Goods(models.Model):
    goods = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.BooleanField(blank=True)

    def __str__(self):
        return self.goods