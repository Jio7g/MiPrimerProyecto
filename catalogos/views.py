from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm


class PaisListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/pais_list.html'
    context_object_name = 'paises'
    paginate_by = 3
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_pais'


class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_pais'


class PaisUpdateView(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')


class PaisDeleteView(LoginRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')

#---------- Departamentos ----------

class DepartamentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'
    paginate_by = 3
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_departamento'


class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamentos_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_departamento'


class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamentos_list')
    login_url = reverse_lazy('login')


class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamentos_list')
    login_url = reverse_lazy('login')

#---------- Municipios ----------

class MunicipioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Municipio
    template_name = 'municipio/municipio_list.html'
    context_object_name = 'municipios'
    paginate_by = 3
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_municipio'


class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipios_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_municipio'


class MunicipioUpdateView(LoginRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipios_list')
    login_url = reverse_lazy('login')


class MunicipioDeleteView(LoginRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'municipio/municipio_confirm_delete.html'
    success_url = reverse_lazy('municipios_list')
    login_url = reverse_lazy('login')