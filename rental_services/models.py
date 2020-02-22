from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    surname = models.CharField(max_length=20)
    given_name = models.CharField(max_length=20)
    gender = models.BooleanField()
    date_of_birth = models.DateField()
    time_created = models.DateTimeField(default=timezone.now)
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE)  # admin who gave this

