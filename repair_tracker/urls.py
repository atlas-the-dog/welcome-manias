from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^customer/(?P<pk>\d+)/edit/$', views.CustomerUpdate.as_view(), name='edit_customer'),
    url(r'^customer/new/$', views.CustomerCreate.as_view(), name='new_customer'),
    url(r'^customer/(?P<pk>\d+)/delete/$', views.CustomerDelete.as_view(), name='delete_customer'),

]