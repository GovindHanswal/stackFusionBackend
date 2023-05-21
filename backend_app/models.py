from django.db import models


class UserForm(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
