from django.urls import path
from . import views
from .app_customer.customer_forms import AddCustomerForm

app_name = 'services'

urlpatterns = [
    path('', views.dash_main, name='service-main'),
    path('tenant/', views.customer_main, name='tenant-main'),
    path('add_customer/', views.AddCustomerView.as_view(), name='add-customer'),
]

