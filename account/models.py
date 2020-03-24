from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20,verbose_name ="手机号")
    image = models.ImageField(upload_to='user/img/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ['id']