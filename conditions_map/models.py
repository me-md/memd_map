from django.db import models

class Conditions(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    state = models.TextField()
