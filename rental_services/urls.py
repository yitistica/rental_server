from django.urls import path
from . import views
from .app_customer.customer_forms import AddCustomerForm

app_name = 'services'

urlpatterns = [
    path('', views.dash_main, name='service-main'),
    path('tenant/', views.customer_main, name='tenant-main'),
    path('add_customer/', views.AddCustomerView.as_view(), name='add-customer'),

    path('property/', views.property_main, name='property-main'),
    path('contract/', views.ContractListView.as_view(), name='contract-main'),
    path('contract/<int:pk>', views.ContractDetailView.as_view(), name='contract-detail'),
    path('contract/<int:pk>/update', views.ContractUpdateView.as_view(), name='contract-update'),
    path('contract/<int:template_id>/delete', views.contract_template_delete, name='contract-delete'),
    path('contract/create/', views.ContractCreateView.as_view(), name='contract-create'),
]

