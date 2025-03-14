from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'


class ServicesView(TemplateView):
    template_name = 'services/services.html'


class ContactView(TemplateView):
    template_name = 'contacts/contacts.html'