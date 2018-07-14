from django.forms import ModelForm
from repair_tracker.models import Customer, Product, Technician

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'surname', 'phone', 'phone_mobile', 'phone_other', 'address']

class TechnicianForm(ModelForm):
    class Meta:
        model = Technician
        fields = ['first_name', 'surname', 'phone', 'phone_other', 'email']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['make', 'model', 'product_type', 'damage', 'notes', 'purchase_date', 'reported_date', 'repaired_date', 'customer', 'technician']