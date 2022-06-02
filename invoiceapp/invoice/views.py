from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('invoice/create_invoice.html')
    context = {
        'name_':'odera'
    }
    return HttpResponse(template.render(context, request))

   