from django.db import models
from django.forms import ModelForm


# Create your models here.
class TrialBalance(models.Model):
    accountNumber = models.CharField(max_length=30)
    accountAssetType = models.CharField(max_length=30)
    accountSubType = models.CharField(max_length=30)
    accountClass = models.CharField(max_length=30)
    accountSubClass = models.CharField(max_length=30)
    beginningBalance = models.FloatField()
    endingBalance = models.FloatField()


class TrialBalanceFile(models.Model):
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)