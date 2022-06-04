from faulthandler import disable
from random import choices
from tkinter import DISABLED
from django.db import models
from django.conf import settings
from django.utils import timezone

#create initial invoice models


class Invoice(models.Model):
    
    
    status_options = [
                    ('Draft','Draft'),
                    ('Pending','Pending'),
                    ('','')
                    ]
    id = models.CharField(primary_key=True,max_length=200)   
    createdAt = models.DateTimeField(auto_now=True)
    paymentDue = models.DateField(blank=True, null=True)
    description = models.TextField()
    paymentTerms =  models.IntegerField(null=True)
    clientName = models.CharField(max_length=200)
    clientEmail = models.EmailField(max_length=200)
    status = models.CharField(max_length=10,choices=status_options,default='')
    total = models.FloatField(default=0.0)
    
    def generate_id(self,length=10):
        """generate random string to be used as invoice id"""
        import string,random
        upper_string =  ''.join(random.choices(string.ascii_uppercase , k = 2))
        digit_string = ''.join(random.choices(string.digits , k = 4))

        rand_id =  upper_string + digit_string
        return rand_id
    
    
    def __str__(self):
        return self.id

    
    
    def generate_due_date(self):
        '''generate payment due date using payment terms'''
        from datetime import datetime,date,timedelta
        
        if self.paymentTerms:
            self.paymentDue = datetime.strptime(self.createdAt,"%m/%d/%y") + timedelta(days=10)
        
    
    
class senderAddress(models.Model):
    
    street =  models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postCode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.street} {self.postCode} {self.country}"

class clientAddress(models.Model):
    street =  models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postCode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.street} {self.postCode} {self.country}"

    
class Items(models.Model):
    
    name =  models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    

   
"""{
    "id": "RT3080",
    "createdAt": "2021-08-18",
    "paymentDue": "2021-08-19",
    "description": "Re-branding",
    "paymentTerms": 1,
    "clientName": "Jensen Huang",
    "clientEmail": "jensenh@mail.com",
    "status": "paid",
    "senderAddress": {
      "street": "19 Union Terrace",
      "city": "London",
      "postCode": "E1 3EZ",
      "country": "United Kingdom"
    },
    "clientAddress": {
      "street": "106 Kendell Street",
      "city": "Sharrington",
      "postCode": "NR24 5WQ",
      "country": "United Kingdom"
    },
    "items": [
      {
        "name": "Brand Guidelines",
        "quantity": 1,
        "price": 1800.90,
        "total": 1800.90
      }
    ],
    "total": 1800.90
  },"""