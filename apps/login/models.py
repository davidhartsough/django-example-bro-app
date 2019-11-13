from django.db import models


class Bro(models.Model):
    broname = models.CharField(max_length=255)
    bropass = models.CharField(max_length=255)
