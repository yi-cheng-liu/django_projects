from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(default=None, null=True)
    latitude = models.FloatField(default=None, null=True)
    longitude = models.FloatField(default=None, null=True)
    description = models.TextField(default=None, null=True)
    justification = models.TextField(default=None, null=True)
    area_hectares = models.FloatField(default=1.0, null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey("Iso", on_delete=models.CASCADE, null=True)
    state = models.ForeignKey("State", on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.name
