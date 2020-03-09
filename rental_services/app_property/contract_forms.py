from bootstrap_modal_forms.forms import BSModalForm
from ..models import Customer
from django.forms import ModelForm
from django.forms import CharField
from rental_services.utils.validators.person_validators import SoftNIDValidator


class D(BSModalForm):
    nid_number = CharField(validators=[SoftNIDValidator()])
    surname = CharField(max_length=20)
    surname.widget.attrs.update({'placeholder': '姓名'})
    class Meta:
        model = Customer
        # fields = ['surname', 'given_name', 'nid_number']
        exclude = ['signed_user', 'gender', 'date_of_birth']


