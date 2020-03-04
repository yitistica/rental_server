from django.db import models
from django.utils import timezone
from .base_models import SignedCommonInfo, Person, Contact
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

    def __str__(self):
        return f"{self.rental_block}_{self.rental_unit}"


class ContractTemplate(models.Model):
    template_id = models.AutoField(primary_key=True, unique=True)
    created_time = models.DateTimeField(auto_now=True)
    template_title = models.CharField(max_length=250)
    template_document = models.TextField(blank=True)

    def __str__(self):
        return self.template_title


# operations
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True, unique=True)
    owner = models.ForeignKey(Owner, default=1, on_delete=models.SET_DEFAULT)
    customer = models.ForeignKey(Customer, default=1, on_delete=models.SET_DEFAULT)
    effective_start_date = models.DateTimeField(null=True)
    effective_end_date = models.DateTimeField(null=True)
    template = models.ForeignKey(ContractTemplate, default=1, on_delete=models.SET_DEFAULT)
    additional_clauses = models.TextField(blank=True)

