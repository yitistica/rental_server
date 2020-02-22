from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_customers, name='rental_services main'),
]

