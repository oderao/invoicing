from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Invoice


def index(request):
    
    "get form data and create invoice in the database "
    template = loader.get_template('invoice/create_invoice.html')
    context = {}
    if request.method == 'POST':
        invoice = Invoice()
        #calculate and set custom default field
        invoice.id = invoice.generate_id()
        invoice.generate_due_date()
        
        if request.POST.get('save_as_draft'):
            #save invoice as draft even with no fields
            
            invoice.status = 'Pending'
            invoice.save()
        if request.POST.get('description') and request.POST.get('clientEmail'):
            invoice=Invoice()
            invoice.description = request.POST.get('description')
            invoice.clientEmail= request.POST.get('client_email')
            invoice.createdAt = request.POST.get('createdAt')
            invoice.paymentTerms = request.POST.get('paymentTerms')
            invoice.status= request.POST.get('status')
            invoice.total = request.POST.get('total')
            invoice.save()
            
            
            return HttpResponse(template.render(context, request))
        
        else:
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))

    # return HttpResponse(template.render(context, request))