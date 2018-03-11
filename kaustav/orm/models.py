from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.ForeignKey('Account_Risk',related_name="acc")
    account_child_id = models.IntegerField(primary_key=True,default=0)
    potential = models.CharField(max_length=200)
    pipeline = models.CharField(max_length=200)
    stage = models.CharField(max_length=200)



class Account_Risk(models.Model):
    account_id = models.IntegerField(primary_key=True, default=0)
    account_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    account_risk = models.CharField(max_length=200)

    def __int__(self):
        return self.account_id
