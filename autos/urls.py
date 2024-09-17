from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'autos'
urlpatterns = [
    path('', TemplateView.as_view(template_name='autos/index.html'),  name='index'),
]
