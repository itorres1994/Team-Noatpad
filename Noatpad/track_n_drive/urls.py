from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit-user', views.edit_user, name='edit_user'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/$', views.car_prof, name='car'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/$', views.tech_prof, name='tech'),
    url(r'^stats-(?P<unique_id>[-\w]+)/$', views.stats, name='stat'),
    url(r'^setting$', views.setting, name='settings'),
    url(r'^add-tech$', views.add_technician1, name='add_technician'),
    url(r'^tech-prof-(?P<unique_id>[-\w]+)/add-tech$', views.add_technician2, name='add_technician'),
    # url(r'^tech-prof-(?P<unique_id>[-\w]+)/add-tech-info$', views.add_technician_info, name='add_technician_info'),
    url(r'^add-car$', views.add_car, name='add_car'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/add-car-info', views.add_car_info, name='add_car_info'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/add-car$', views.edit_car, name='add_car'),
    # url(r'^car-prof-(?P<unique_id>[-\w]+)/add-future-repair$', views.add_future_repair, name='add_future_repairs'),
    url(r'^car-prof-(?P<unique_id>[-\w]+)/add-future-repair$', views.add_future_repair, name='add_future_repairs'),
    # url(r'^car-prof-(?P<unique_id>[-\w]+)/add-repair$', views.add_repair, name='add_repair'),
    # url(r'^setting/add-phone$', views.add_phone, name='add_phone'),
    # url(r'^setting/add-email$', views.add_email, name='add_email'),
    # url(r'^setting/add-user-info$', views.add_user_info, name='add_user_info'),
]
