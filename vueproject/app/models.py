from django.db import models

# Create your models here.

class User(models.Model):
    UserName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)

class Gpxx(models.Model):
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200)
    f8 = models.CharField(max_length=200)
    f9 = models.CharField(max_length=200)
    f10 = models.CharField(max_length=200)
    f11 = models.CharField(max_length=200)
    f12 = models.CharField(max_length=200)
    f13 = models.CharField(max_length=200)
    f14 = models.CharField(max_length=200)
    f15 = models.CharField(max_length=200)
    f16 = models.CharField(max_length=200)
    f17 = models.CharField(max_length=200)
    f18 = models.CharField(max_length=200)
    f19 = models.CharField(max_length=200)
    f20 = models.CharField(max_length=200)
    f21 = models.CharField(max_length=200)
    f22 = models.CharField(max_length=200)
    f23 = models.CharField(max_length=200)
    f24 = models.CharField(max_length=200)
    f25 = models.CharField(max_length=200)
    f26 = models.CharField(max_length=200)
    f27 = models.CharField(max_length=200)
    f28 = models.CharField(max_length=200)
    f29 = models.CharField(max_length=200)



class gp_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    dm = models.CharField(max_length=200)
    sj = models.CharField(max_length=200)
    kp = models.CharField(max_length=200)
    sp = models.CharField(max_length=200)
    zg = models.CharField(max_length=200)
    zd = models.CharField(max_length=200)
    cjl = models.CharField(max_length=200)
    cle = models.CharField(max_length=200)
    zf = models.CharField(max_length=200)
    zdf = models.CharField(max_length=200)
    zdje = models.CharField(max_length=200)
    hs = models.CharField(max_length=200)
    