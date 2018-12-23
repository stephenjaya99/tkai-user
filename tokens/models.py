from django.db import models

# Create your models here.
class Token(models.Model):
	payload = models.TextField()
