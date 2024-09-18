from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from autos.models import Auto, Make

class MainView(LoginRequiredMixin, ListView):
    model = Auto

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['make_count'] = Make.objects.count()
        return ctx

class MakeView(LoginRequiredMixin, ListView):
    model = Make

class MakeMixin:
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeCreate(MakeMixin, LoginRequiredMixin, CreateView):
    pass

class MakeUpdate(MakeMixin, LoginRequiredMixin, UpdateView):
    pass

class MakeDelete(MakeMixin, LoginRequiredMixin, DeleteView):
    pass

class AutoMixin:
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoCreate(AutoMixin, LoginRequiredMixin, CreateView):
    pass

class AutoUpdate(AutoMixin, LoginRequiredMixin, UpdateView):
    pass

class AutoDelete(AutoMixin, LoginRequiredMixin, DeleteView):
    pass
