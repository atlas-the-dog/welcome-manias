from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the repair-tracker homepage.")

class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'surname', 'phone', 'phone_mobile', 'phone_other', 'address']

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['first_name', 'surname', 'phone', 'phone_mobile', 'phone_other', 'address']
    template_name_suffix = '_update_form'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')