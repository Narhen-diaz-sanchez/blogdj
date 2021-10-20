#
from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/',
        views.UserPageListView.as_view(),
        name='perfil',
    ),
]
