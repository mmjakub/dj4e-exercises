from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Auto, Make


class AutoListView(LoginRequiredMixin, ListView):
    model = Auto
    template_name = 'autos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['make_count'] = Make.objects.count()
        return context

class AutoEditViewMixin(LoginRequiredMixin):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoCreateView(AutoEditViewMixin, CreateView): pass
class AutoDeleteView(AutoEditViewMixin, DeleteView): pass
class AutoUpdateView(AutoEditViewMixin, UpdateView): pass

class MakeListView(LoginRequiredMixin, ListView):
    model = Make
    template_name = 'autos/makes.html'

class MakeEditViewMixin(LoginRequiredMixin):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')

class MakeCreateView(MakeEditViewMixin, CreateView): pass
class MakeDeleteView(MakeEditViewMixin, DeleteView): pass
class MakeUpdateView(MakeEditViewMixin, UpdateView): pass


