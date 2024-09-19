from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from cats.models import Breed, Cat 

class CatListView(LoginRequiredMixin, ListView):
    model = Cat
