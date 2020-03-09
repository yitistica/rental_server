from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class CommonInfo(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SignedCommonInfo(CommonInfo):
    signed_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Person(SignedCommonInfo):
    surname = models.CharField(max_length=20, blank=False)
    given_name = models.CharField(max_length=20, blank=False)
    nid_number = models.CharField(max_length=20, blank=False)
    gender = models.CharField(max_length=20, choices=[('M', '男'), ('F', '女')], default='F')

    date_of_birth = models.DateField(null=True)

    class Meta:
        abstract = True


class Contact(models.Model):
    primary_contact_number = models.CharField(max_length=20, blank=True)
    secondary_contact_number = models.CharField(max_length=20, blank=True)
    emergency_contact_name = models.CharField(max_length=20, blank=True)
    emergency_contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    wechat_account = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True

