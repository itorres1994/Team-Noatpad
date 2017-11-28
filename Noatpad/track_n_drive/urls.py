from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/$', views.car_prof, name='car'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/$', views.tech_prof, name='tech'),
    url(r'^stats-(?P<unique_id>[-\w]+)/$', views.stats, name='stat'),
    url(r'^setting$', views.setting, name='settings'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/edit$', views.add_technician, name='add_technician'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/edit$', views.add_technician_info, name='add_technician_info'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/$', views.add_car, name='add_car'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/$', views.add_future_repairs, name='add_future_repairs'),
]
