from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm
from .models import Contact

class ResumePage(View):
    def get (self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render (request, 'index.html', context)
    
    def post (self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        responses = Contact.objects.all()

        context = {
            'form': form,
            'response_list': responses,
        }
        if form.is_valid():
            new_response = form.save()
            form= ContactForm()

            messages.info(request, "Message sent! View all messages at '/responses' " )
            return HttpResponseRedirect("/")
            return render (request, 'index.html', context) 
    
class Responses(View):
    def get (self, request, *args, **kwargs):
         responses = Contact.objects.all()

         context = {
            'response_list': responses,
         }
         return render (request, 'responses.html', context)