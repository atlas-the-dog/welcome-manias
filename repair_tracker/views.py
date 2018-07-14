from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, TechnicianForm, ProductForm

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the repair-tracker homepage.")

@login_required
def customer_edit(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'repair_tracker/customer.html', {'form': form})