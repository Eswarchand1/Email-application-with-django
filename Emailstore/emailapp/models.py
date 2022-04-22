from django.db import models

# Create your models here.
from django.db.models import Model


class login(models.Model):
    user_name = models.EmailField()
    password  = models.CharField(max_length=30)
    def __str__(self):
        return self.user_name + " " + self.password


class signUp(models.Model):
    username = models.CharField(max_length=30)
    semail   = models.EmailField()
    spass    = models.CharField(max_length=30)
    srpass   = models.CharField(max_length=30)

    def __str__(self):
        return self.username + " " + self.semail + " " +self.spass + " " + self.srpass

class sendMsg(models.Model):

    cruser = models.EmailField()
    sendmail     = models.EmailField()
    sendsubject  = models.CharField(max_length=300)
    sendtext     = models.TextField()

    def __str__(self):
        return self.sendmail + " " + self.sendsubject + " " +self.sendtext

class receiveMsg(models.Model):
    cruser         = models.EmailField()
    receivemail    = models.EmailField()
    receivesubject = models.CharField(max_length=300)
    receivetext    = models.TextField()

    def __str__(self):
        return self.receivemail + " " + self.receivesubject + " " +self.receivetext


class setContacts(models.Model):
    cemailholder = models.EmailField()
    cusername = models.CharField(max_length=30)
    cemail    = models.EmailField()
    cphonenumber = models.CharField(max_length=13)
    caddress = models.TextField()

    def __str__(self):
        return self.cusername + " " + self.cemail

class getprofileData(models.Model):
    choosefile       = models.ImageField(upload_to='media/',blank=True,null=True)
    pname            = models.CharField(max_length=30)
    pmail            = models.EmailField()
    pdate            = models.DateField()
    pcountry         = models.CharField(max_length=30)
    paddress         = models.TextField()
    pnumber          = models.CharField(max_length=30)
    pprofession      = models.CharField(max_length=30)
    ppass            = models.CharField(max_length=30 ,blank=True)
    prpass           = models.CharField(max_length=30 ,blank=True)
    pid              = models.ImageField(upload_to='media/')


    def __str__(self):
        return self.pname + " " + self.pmail + " " + self.pcountry + " " + self.paddress + " " + self.pnumber + " " + self.pprofession + " " + self.ppass + " " + self.prpass

    def save(self):  # ALL the signature
        super(getprofileData, self).save()


class usersLog(models.Model):
    usmail = models.EmailField()

    def __str__(self):
        return self.usmail

class walletBalance(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    wallet = models.CharField(max_length=30)

    def __str__(self):
        return self.wallet + " " + self.id




