from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, validate_email

class Technician(models.Model):
    first_name  = models.CharField(max_length=200, verbose_name = _('ονομα'))
    surname  = models.CharField(max_length=200, verbose_name = _('επιθετο'))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name = _('σταθερό'))
    phone_other = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name = _('αλλο'))
    email  = models.CharField(validators=[validate_email], max_length=200, verbose_name = _('email'))

    class Meta:
        verbose_name = _('Τεχνικος')
        verbose_name_plural = _('Τεχνικοι')

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.surname, self.phone)

class Customer(models.Model):
    first_name = models.CharField(max_length=200, verbose_name = _('ονομα'))
    surname = models.CharField(max_length=200, verbose_name = _('επιθετο'))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name = _('σταθερό'))
    phone_mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name = _('κινητο'))
    phone_other = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name = _('αλλο'))
    address = models.CharField(max_length=200, verbose_name = _('διευθυνση'))

    class Meta:
        verbose_name = _('Πελατης')
        verbose_name_plural = _('Πελατες')

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.surname, self.phone)

class Product(models.Model):
    make = models.CharField(max_length=200, verbose_name = _('μαρκα'))
    model = models.CharField(max_length=200, verbose_name = _('μοντέλο'))
    product_type = models.CharField(max_length=200, verbose_name = _('προϊόν'))
    damage = models.TextField(verbose_name = _('βλαβη'))
    notes = models.TextField(blank=True, verbose_name = _('μαρκα'))
    purchase_date = models.DateField(verbose_name = _('ημερομηνία αγοράς'))
    reported_date = models.DateTimeField(verbose_name = _('ημερομηνία αναφοράς'))
    repaired_date = models.DateTimeField(blank=True, null=True, verbose_name = _('ημερομηνία επισκευής'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = _('πελάτης'))
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True, verbose_name = _('τεχνικός'))

    class Meta:
        verbose_name = _('ΠΡΟΙΟΝ')
        verbose_name_plural = _('ΠΡΟΙΟΝΤΑ')

    def __str__(self):
        return '{} {} ({}) - {}, ΕΠΙΣΚΕΥΑΣΤΗΚΕ {}'.format(self.make, self.model, self.product_type, self.customer, self.technician)