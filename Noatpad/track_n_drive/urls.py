from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/$', views.car_prof, name='car'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/$', views.tech_prof, name='tech'),
]
