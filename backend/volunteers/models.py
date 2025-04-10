from django.db import models

# Volunteer Model
class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    project = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - ${self.name}"
