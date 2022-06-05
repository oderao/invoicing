from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='create-invoice'),
    path(r'list_invoice', views.invoice_list, name='list_invoice')
]