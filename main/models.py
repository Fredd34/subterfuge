from django.db import models

class credentials(models.Model):
    source      = models.CharField(max_length=300)
    username    = models.CharField(max_length=300)
    password    = models.CharField(max_length=300)
    date        = models.CharField(max_length=300)