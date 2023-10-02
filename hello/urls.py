from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('cookie', views.cookie, name='cookie'),
    path('sessfun', views.sessfun, name='sessfun'),
]
