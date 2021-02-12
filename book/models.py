from django.db import models

# Create your models here.



class MoneyModel(models.Model):
    human_id = models.IntegerField()
    year = models.CharField(max_length=10)
    workplace = models.CharField(max_length=50)
    janu = models.IntegerField(null=True, blank=True, default=0)
    feb = models.IntegerField(null=True, blank=True, default=0)
    mar = models.IntegerField(null=True, blank=True, default=0)
    apl = models.IntegerField(null=True, blank=True, default=0)
    may = models.IntegerField(null=True, blank=True, default=0)
    jun = models.IntegerField(null=True, blank=True, default=0)
    jul = models.IntegerField(null=True, blank=True, default=0)
    aug = models.IntegerField(null=True, blank=True, default=0)
    sep = models.IntegerField(null=True, blank=True, default=0)
    octr = models.IntegerField(null=True, blank=True, default=0)
    nov = models.IntegerField(null=True, blank=True, default=0)
    dec = models.IntegerField(null=True, blank=True, default=0)