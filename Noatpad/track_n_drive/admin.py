from django.contrib import admin

# Register your models here.

from .models import Car, Phone, PhoneTimings, Email, EmailTimings, Settings, TechAddedInfo, Technician, Repair, UserAddedInfo, Notifications, License, Insurance, User

admin.site.register(Car)
admin.site.register(Phone)
admin.site.register(PhoneTimings)
admin.site.register(Email)
admin.site.register(EmailTimings)
admin.site.register(Settings)
admin.site.register(TechAddedInfo)
admin.site.register(Technician)
admin.site.register(Repair)
admin.site.register(UserAddedInfo)
admin.site.register(Notifications)
admin.site.register(License)
admin.site.register(Insurance)
admin.site.register(User)
