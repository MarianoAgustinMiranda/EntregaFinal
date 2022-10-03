from unicodedata import name
from django.contrib.auth.views import LogoutView
from django.urls import path

from UserInmobiliaria.views import *

urlpatterns = [
    path('login/', login_request, name= 'UserInmobiliariaLogin'),
    path('registro/', register, name= 'UserInmobiliariaRegister'),
    path('logout/', LogoutView.as_view(template_name='UserInmobiliaria/logout.html'), name= 'UserInmobiliariaLogout'),
    path('editar/', editar_usuario, name= 'UserInmobiliariaEditar'),
    path('avatar/', upload_avatar, name='UserInmobiliariaAvatar'),
]