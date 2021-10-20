import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
from applications.entradas.models import Entry
from .forms import SuscribersForm, ContactForm
from .models import Suscribers, Contact


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # Contexto para los articulos en portada
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # Contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # enviamos formulario de suscripción
        context["form"] = SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'
    #model = Suscribers
    # se redefine el form_valid para que una vez valide el formulario recargue la página principal con el reverse

    def form_valid(self, form):
        suscriber = Suscribers(
            email = form.cleaned_data['email']
        )
        suscriber.save()
        return HttpResponseRedirect(reverse('home_app:index', ))


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
    #model = Suscribers
    # se redefine el form_valid para que una vez valide el formulario recargue la página principal con el reverse

    def form_valid(self, form):
        contact = Contact(
            full_name = form.cleaned_data['full_name'],
            email = form.cleaned_data['email'],
            message = form.cleaned_data['message']
        )
        contact.save()
        return HttpResponseRedirect(reverse('home_app:index', ))
