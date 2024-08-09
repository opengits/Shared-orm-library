from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Setting(models.Model):
    is_notification_enabled = models.BooleanField(default=True)
    is_new_dashboard_enabled = models.BooleanField(default=False)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.timezone
