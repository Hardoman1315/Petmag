from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)  # +7(999)999-99-99
    name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.phone_number