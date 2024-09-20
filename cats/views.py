from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from cats.models import Breed, Cat 

class BreedListView(LoginRequiredMixin, ListView):
    model = Breed

class CatListView(LoginRequiredMixin, ListView):
    model = Cat

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['breed_count'] = len(Breed.objects.all())
        return ctx

class BreedMixin:
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class BreedCreateView(BreedMixin, LoginRequiredMixin, CreateView):
    pass

class BreedUpdateView(BreedMixin, LoginRequiredMixin, UpdateView):
    pass

class BreedDeleteView(BreedMixin, LoginRequiredMixin, DeleteView):
    pass

class CatMixin:
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class CatCreateView(CatMixin, LoginRequiredMixin, CreateView):
    pass

class CatUpdateView(CatMixin, LoginRequiredMixin, UpdateView):
    pass

class CatDeleteView(CatMixin, LoginRequiredMixin, DeleteView):
    pass
