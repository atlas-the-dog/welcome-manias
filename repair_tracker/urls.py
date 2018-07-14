from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),

]