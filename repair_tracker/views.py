from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Customer, Product, Technician

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the repair-tracker homepage.")

# Customer views
class CustomerDetail(DetailView):
    model = Customer

class CustomerListView(ListView):
    model = Customer
    paginate_by = 100  # if pagination is desired

class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'surname', 'phone', 'phone_mobile', 'phone_other', 'address']
    
    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.object.pk})

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['first_name', 'surname', 'phone', 'phone_mobile', 'phone_other', 'address']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.object.pk})

class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')

# Product views
class ProductDetail(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

class ProductCreate(CreateView):
    model = Product
    fields = ['make', 'model', 'product_type', 'damage', 'notes', 'purchase_date', 'reported_date', 'repaired_date', 'customer', 'technician']
    
    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.object.pk})

class ProductUpdate(UpdateView):
    model = Product
    fields = ['make', 'model', 'product_type', 'damage', 'notes', 'purchase_date', 'reported_date', 'repaired_date', 'customer', 'technician']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

# Technician views
class TechnicianDetail(DetailView):
    model = Technician

class TechnicianListView(ListView):
    model = Technician
    paginate_by = 100  # if pagination is desired

class TechnicianCreate(CreateView):
    model = Technician
    fields = ['first_name', 'surname', 'phone', 'phone_other', 'email']
    
    def get_success_url(self):
        return reverse_lazy('technician_detail', kwargs={'pk': self.object.pk})

class TechnicianUpdate(UpdateView):
    model = Technician
    fields = ['first_name', 'surname', 'phone', 'phone_other', 'email']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('technician_detail', kwargs={'pk': self.object.pk})

class TechnicianDelete(DeleteView):
    model = Technician
    success_url = reverse_lazy('technician_list')

