from django.db import models
from django.utils import timezone
from .base_models import SignedCommonInfo, Person, Contact
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Customer(Person, Contact):
    cust_id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return f"{self.cust_id}_{self.surname}{self.given_name}"


class Manager(Person, Contact):
    manager_id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return f"{self.manager_id}_{self.surname}{self.given_name}"


class Owner(Person, Contact):
    owner_id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return f"{self.owner_id}_{self.surname}{self.given_name}"


class RentalUnit(SignedCommonInfo):
    rental_id = models.AutoField(primary_key=True, unique=True)
    rental_unit = models.CharField(max_length=100, blank=True)
    rental_block = models.CharField(max_length=100, blank=True)
    rental_address = models.CharField(max_length=100, blank=True)
    rental_owner = models.ForeignKey(Owner, default=2, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.rental_block}_{self.rental_unit}"


class ContractTemplate(models.Model):
    template_id = models.AutoField(primary_key=True, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    create_author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT, related_name='create_author')
    update_author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT, related_name='update_author')
    template_title = models.CharField(max_length=250)
    template_document = models.TextField(blank=True)

    def __str__(self):
        return self.template_title

    def get_absolute_url(self):
        return reverse('services:contract-detail', kwargs={'pk': self.pk})


class TermStructure(models.Model):
    term_id = models.AutoField(primary_key=True, unique=True)
    associate_template = models.ForeignKey(Customer, default=1, on_delete=models.SET_DEFAULT)
    additional_provisions = models.TextField(blank=True)
    regularity = JSONField()


# operations
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True, unique=True)
    rental_id = models.ForeignKey(RentalUnit, default=1, on_delete=models.SET_DEFAULT)
    customer = models.ForeignKey(Customer, default=1, on_delete=models.SET_DEFAULT)
    effective_start_date = models.DateTimeField(null=True)
    effective_end_date = models.DateTimeField(null=True)
    term_structure = models.ForeignKey(TermStructure, default=1, on_delete=models.SET_DEFAULT)
    effective = models.BooleanField(default=True)


class RegularityType(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


class Usage(models.Model):
    record_id = models.AutoField(primary_key=True, unique=True)
    rental_id = models.ForeignKey(RentalUnit, default=1, on_delete=models.SET_DEFAULT)
    regularity_type = models.ForeignKey(RegularityType, default=1, on_delete=models.SET_DEFAULT)
    start_date = models.DateField()
    end_date = models.DateField()
    usage = models.FloatField()



