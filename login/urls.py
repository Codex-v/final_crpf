from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login', views.login, name='login')
    # path('logout', views.logOut),
    
]
