from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView
)
# Create your views here.
from .models import Favorites


class UserPageListView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy ('users_app:user-login')
    
    
    
    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)