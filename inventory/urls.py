from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_inventory$', add_inventory, name='add_inventory'),
    url(r'^update_inventory/(?P<pk>\d+)$', update_inventory, name='update_inventory'),
url(r'^delete_inventory/(?P<pk>\d+)$', delete_inventory, name='delete_inventory'),
]
