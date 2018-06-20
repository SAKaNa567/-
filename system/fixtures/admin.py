# Register your models here.
from django.contrib import admin

from .models import Goods,Category

admin.site.register(Goods)
admin.site.register(Category)