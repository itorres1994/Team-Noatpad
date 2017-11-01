from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^car-detail:(?P<unique_id>[\w]+)/$', views.car_prof, name='car'),
]
