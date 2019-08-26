from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=20)


class UserModel(model.Model):
    name = models.CharField(max_length=20)


class TollModel(model.Model):
    name = models.CharField(max_length=20)