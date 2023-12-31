from django.db import models

# Create your models here.
class user_info(models.Model):
    user_email = models.CharField(max_length=150, null=True)
    user_name = models.CharField(max_length=100)
    user_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=150, null=True)
    user_profileimage = models.CharField(max_length=200, null=True)
    user_banner = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user_name}"
