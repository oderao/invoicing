from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Invoice


def index(request):
    model = Invoice
    fields = ['description']
    template = loader.get_template('invoice/create_invoice.html')
    context = {
        'name_':'odera'
    }
    return HttpResponse(template.render(context, request))

    return HttpResponse("Hello, world. You're at the invoice index.")