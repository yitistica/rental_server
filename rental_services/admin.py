from django.contrib import admin
from .models import Customer, Manager, RentalUnit, Owner, ContractTemplate, Contract
# Register your models here.

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Owner)
admin.site.register(RentalUnit)
admin.site.register(ContractTemplate)
admin.site.register(Contract)
