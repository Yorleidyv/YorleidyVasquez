from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tratamiento
from .forms import TratamientoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound



def inicio(request):
    return render(request, 'inicio/inicio.html', context={'key': 'value'})


def tratamiento(request):
    return render(request, 'inicio/tratamiento.html', context={'key': 'value'})

def sobremi(request):
    return render(request, 'inicio/sobremi.html', context={'key': 'value'})

class TratamientoListView(ListView):
    model = Tratamiento
    template_name = 'tratamiento_list.html'
    context_object_name = 'tratamientos'

    def get_queryset(self):
        nombre_tratamiento = self.request.GET.get('nombre', '')

        if nombre_tratamiento:
            queryset = Tratamiento.objects.filter(nombre__icontains=nombre_tratamiento)
        else:
            queryset = Tratamiento.objects.all()

        return queryset


class TratamientoDetailView(DetailView):
    model = Tratamiento
    template_name = 'inicio/tratamiento_detail.html'
    context_object_name = 'tratamiento'

    def render_to_response(self, context, **response_kwargs):
        if self.get_object() is None:
            return HttpResponseNotFound("Tratamiento no encontrado")
        return super().render_to_response(context, **response_kwargs)


class TratamientoCreateView(LoginRequiredMixin, CreateView):
    model = Tratamiento
    template_name = 'inicio/tratamiento_form.html'
    form_class = TratamientoForm
    success_url = reverse_lazy('tratamiento-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


# class TratamientoUpdateView(LoginRequiredMixin, UpdateView):
#     model = Tratamiento
#     template_name = 'inicio/tratamiento_form.html'
#     form_class = TratamientoForm
#     success_url = reverse_lazy('tratamiento-list')

class TratamientoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tratamiento
    form_class = TratamientoForm 
    template_name = 'inicio/tratamiento_detail.html'
    success_url = reverse_lazy('tratamiento-list')

    def get_object(self, queryset=None):
        return Tratamiento.objects.get(pk=self.kwargs['pk'])
 

class TratamientoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tratamiento
    template_name = 'inicio/tratamiento_confirm_delete.html'
    success_url = reverse_lazy('tratamiento-list')