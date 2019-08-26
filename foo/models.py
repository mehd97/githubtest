from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=20)


class UserModel(model.Model):
    name = models.CharField(max_length=20)


class ToolModel(model.Model):
    name = models.CharField(max_length=20)
<<<<<<< HEAD
    age = models.CharField(max_length=20)

class test:
    pass
=======
    age = models.CharField(max_length=20)
>>>>>>> 0381f6d8b011a0cda0950232088c7274f8c5b7dd
