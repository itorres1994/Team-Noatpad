from django.contrib import admin

# Register your models here.

from .models import Car, Phone, PhoneTimings, Email, EmailTimings, Settings, TechAddedInfo, Technician, Repair, \
    UserAddedInfo, Notifications, License, Insurance, User, FutureRepair

admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(TechAddedInfo)
admin.site.register(Repair)
# admin.site.register(FutureRepair)


@admin.register(FutureRepair)
class FutureRepairAdmin(admin.ModelAdmin):
    list_display = ('name', 'technician', 'date_of_repair')


class CarInstanceInlineInsurance(admin.TabularInline):
    model = Insurance
    extra = 0


class CarInstanceInlineRepair(admin.TabularInline):
    model = Repair
    extra = 0


class CarInstanceInlineFutureRepair(admin.TabularInline):
    model = FutureRepair
    extra = 0


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('vin_number', 'make', 'model', 'year', 'color', 'registration')
    inlines = [CarInstanceInlineInsurance, CarInstanceInlineRepair,
               CarInstanceInlineFutureRepair]


@admin.register(PhoneTimings)
class PhoneTimingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'frequency', 'reminder')


@admin.register(EmailTimings)
class EmailTimingsAdmin(admin.ModelAdmin):
    list_display = ('email', 'frequency', 'reminder')


class NotificationsInstanceInline(admin.TabularInline):
    model = FutureRepair
    extra = 0


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    inlines = [NotificationsInstanceInline]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')


class TechnicianInstanceInline(admin.TabularInline):
    model = TechAddedInfo
    extra = 0


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'street', 'city', 'company')
    inlines = [TechnicianInstanceInline]


class UserInstanceInlineInfo(admin.TabularInline):
    model = UserAddedInfo
    extra = 0


class UserInstanceInlineCars(admin.TabularInline):
    model = Car
    extra = 0


class UserInstanceInlinePhones(admin.TabularInline):
    model = Phone
    extra = 0


class UserInstanceInlineEmails(admin.TabularInline):
    model = Email
    extra = 0


class UserInstanceInlineNotifications(admin.TabularInline):
    model = Notifications
    extra = 0


class UserInstanceInlineSettings(admin.TabularInline):
    model = Settings
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname')
    inlines = [UserInstanceInlineInfo, UserInstanceInlineCars,
               UserInstanceInlinePhones, UserInstanceInlineEmails,
               UserInstanceInlineNotifications, UserInstanceInlineSettings]


# admin.site.register(Technician)
admin.site.register(UserAddedInfo)
admin.site.register(License)
admin.site.register(Insurance)
# admin.site.register(User)
