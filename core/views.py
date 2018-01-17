# coding=utf-8

from django.shortcuts import render

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    sucess = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        sucess = True

    context = {
        'form': form,
        'sucess': sucess,
    }
    
    return render(request, 'contact.html', context)
