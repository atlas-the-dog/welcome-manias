from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Customer

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the repair-tracker homepage.")

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