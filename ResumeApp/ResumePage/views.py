from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.views.generic import TemplateView, CreateView


class ResumePage(TemplateView):
    template_name = 'index.html'
