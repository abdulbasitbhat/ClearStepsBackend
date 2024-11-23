from django.db import models

class Personality(models.Model):
    email = models.CharField(max_length=100)
    personality = models.TextField()
    def __str__(self):
        return self.email

