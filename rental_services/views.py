from django.shortcuts import render
from .app_customer.customer_forms import AddCustomerForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Customer, RentalUnit

from .utils.info_extract import nid_info_extract


# Create your views here.


def dash_main(request):
    return render(request, 'rental_services/service_base.html')


# def customer_main(request):
#     return render(request, 'rental_services/tenant.html', )


def customer_main(request):
    query_results = Customer.objects.all()

    context = {
        'results': query_results
    }
    # all_fields = Customer._meta.get_fields()
    # table = dict()
    # for result in query_results:
    #     for field in all_fields:
    #         table[field] = result.field

    return render(request, 'rental_services/tenant.html', context)


class AddCustomerView(BSModalCreateView):
    form_class = AddCustomerForm
    template_name = 'rental_services/modal_1.html'
    success_message = 'Success.'
    success_url = reverse_lazy('services:tenant-main')

    def post(self, request, *args, **kwargs):
        form = AddCustomerForm(request.POST)
        # add additional fields:
        if form.is_valid():
            form.request = request
            obj = form.save(commit=False)
            obj.signed_user = request.user
            obj.gender = nid_info_extract.get_gender_from_nid(nid=form.cleaned_data['nid_number'])
            obj.date_of_birth = nid_info_extract.get_dob(nid=form.cleaned_data['nid_number'])
            # form.cleaned_data['signed_user'] = request.user.pk
            # form.cleaned_data['gender'] = nid_info_extract.get_gender_from_nid(nid=form.cleaned_data['nid_number'])
            # form.cleaned_data['date_of_birth'] = nid_info_extract.get_gender_from_nid(nid=form.cleaned_data['nid_number'])
            print(form)
            form.save()
            form = AddCustomerForm()
        context = {"form": form}
        return render(request, self.template_name, context)


def property_main(request):
    query_results = RentalUnit.objects.all()

    print(query_results)
    context = {
        'results': query_results
    }
    # all_fields = Customer._meta.get_fields()
    # table = dict()
    # for result in query_results:
    #     for field in all_fields:
    #         table[field] = result.field

    return render(request, 'rental_services/property.html', context)


