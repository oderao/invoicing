from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Invoice


def index(request):
    
    "get form data and create invoice in the database "
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            invoice=Invoice()
            invoice.title= request.POST.get('title')
            invoice.content= request.POST.get('content')
            invoice.save()
            
            return render(request, 'invoice/create_invoice.html')  

        else:
                return render(request,'posts/create_invoice.html')

    # return HttpResponse(template.render(context, request))