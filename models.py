
from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'


class User_insertion(models.Model):
    Last_name = models.CharField(max_length=50)
    First_name =models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.Last_name, self.First_name, self.Country , self. City, self.Address, self.Description

    class Meta:
        db_table = "Properties"

