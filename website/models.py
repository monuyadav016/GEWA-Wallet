from django.db import models

class ContactPage(models.Model):
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return "{0}'s Message".format(self.name)