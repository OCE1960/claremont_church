from django.shortcuts import render;
from django.views import generic;

from ..tasks import add, send_email

def index(request):
   
    # Render the HTML template index.html with the data in the context variable
    add.delay(14,7)
    send_email.delay_on_commit(15641)
    return render(request, 'cms/index.html')
