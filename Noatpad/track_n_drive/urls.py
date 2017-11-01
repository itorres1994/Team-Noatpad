from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^car-prof-(?P<id>)/$', views.car_prof, name='car'),
]
