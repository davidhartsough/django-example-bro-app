from django.db import models
from apps.login.models import Bro


class Expression(models.Model):
    text = models.CharField(max_length=255)
    bro = models.ForeignKey(Bro, on_delete=models.CASCADE)


class Shout(models.Model):
    expression = models.ForeignKey(Expression, on_delete=models.CASCADE)
    bro = models.ForeignKey(Bro, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
