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

    path('product/', views.ProductListView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name='product_detail'),
    url(r'^product/(?P<pk>\d+)/edit/$', views.ProductUpdate.as_view(), name='edit_product'),
    url(r'^product/new/$', views.ProductCreate.as_view(), name='new_product'),
    url(r'^product/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='delete_product'),

    path('technician/', views.TechnicianListView.as_view(), name='technician_list'),
    url(r'^technician/(?P<pk>\d+)/$', views.TechnicianDetail.as_view(), name='technician_detail'),
    url(r'^technician/(?P<pk>\d+)/edit/$', views.TechnicianUpdate.as_view(), name='edit_technician'),
    url(r'^technician/new/$', views.TechnicianCreate.as_view(), name='new_technician'),
    url(r'^technician/(?P<pk>\d+)/delete/$', views.TechnicianDelete.as_view(), name='delete_technician'),

]