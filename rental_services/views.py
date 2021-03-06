from django.shortcuts import render, redirect
from .app_customer.customer_forms import AddCustomerForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Customer, RentalUnit, ContractTemplate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .utils.info_extract import nid_info_extract
from django.contrib import messages
from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers
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


class ContractSerializer(serializers.ModelSerializer):
    create_time_str = serializers.SerializerMethodField()
    update_time_str = serializers.SerializerMethodField()
    short_template_str = serializers.SerializerMethodField()

    class Meta:
        model = ContractTemplate
        fields = '__all__'

    def get_create_time_str(self, obj):
        return obj.create_time.strftime("%Y/%m/%d %H:%M")

    def get_update_time_str(self, obj):
        return obj.update_time.strftime("%Y/%m/%d %H:%M")

    def get_short_template_str(self, obj):
        if len(obj.template_document) > 100:
            return obj.template_document[0:100] + '...'
        else:
            return obj.template_document


class ContractListView(ListView):
    model = ContractTemplate
    template_name = 'rental_services/contract.html'
    context_object_name = 'contract_templates'
    ordering = ['-update_time']
    queryset = ContractTemplate.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract_templates = context['contract_templates']
        contract_templates = ContractSerializer(contract_templates, many=True)

        context['contract_templates'] = contract_templates.data

        # print(context[ContractListView.context_object_name].apply())
        return context


# class ContractListRetrieveAPIView(ListView):
#     queryset = ContractTemplate.objects.all().order_by('-update_time')
#     # serializer = ContractSerializer(queryset, many=True)
#     template_name = 'rental_services/contract.html'


class ContractDetailView(DetailView):
    model = ContractTemplate


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = ContractTemplate
    fields = ['template_title', 'template_document']

    def form_valid(self, form):
        form.instance.create_author = self.request.user
        form.instance.update_author = self.request.user
        return super().form_valid(form)


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = ContractTemplate
    fields = ['template_title', 'template_document']

    def form_valid(self, form):
        form.instance.update_author = self.request.user
        return super().form_valid(form)


def contract_template_delete(request, template_id):
    item = ContractTemplate.objects.get(template_id=template_id)

    if request.method == 'POST':
        item.delete()
        messages.warning(request, f'contract {template_id} is deleted.')

    return redirect('services:contract-main')


class ContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ContractTemplate
    success_url = reverse_lazy('services:contract-main')

    def test_func(self):
        return True

