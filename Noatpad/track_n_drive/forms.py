from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

from .models import Technician, TechAddedInfo, Car, CarAddedInfo, FutureRepair, Repair, Phone, Email, \
    ProfileAddedInfo, Profile, EmailTimings, PhoneTimings, Notifications


# ModelForm automatically includes all fields and help texts, exclude is used to
# specifically exclude those fields, and labels overrides the default labels.
# Any info specified here overrides what is shown on models.py
class AddTechnicianForm(ModelForm):
    class Meta:
        model = Technician
        exclude = {'unique_id', 'profile'}
        labels = {'fname': _('First Name'), 'lname': _('Last Name'), }


class AddTechAddedInfoForm(ModelForm):
    class Meta:
        model = TechAddedInfo
        exclude = {'tech'}


class AddCarForm(ModelForm):
    class Meta:
        model = Car
        exclude = {'unique_id', 'profile'}
        help_texts = ''


class EditCarForm(ModelForm):
    class Meta:
        model = CarAddedInfo
        exclude = {'car'}


class AddFutureRepairForm(ModelForm):
    class Meta:
        model = FutureRepair
        exclude = {'unique_id', 'car'}

    def __init__(self, profile, *args, **kwargs):
        super(AddFutureRepairForm, self).__init__(*args, **kwargs)
        self.fields['date_of_repair'].widget = SelectDateWidget()
        self.fields['technician'].queryset = Technician.objects.filter(profile=profile)


class AddNotification(ModelForm):
    class Meta:
        model = Notifications
        exclude = {'profile', 'unique_id'}

    def __init__(self, *args, **kwargs):
        super(AddNotification, self).__init__(*args, **kwargs)
        self.fields['date'].widget = SelectDateWidget()


class EditFutureRepairForm(ModelForm):
    class Meta:
        model = FutureRepair
        exclude = {'unique_id', 'car', 'reminder1', 'reminder2'}

    def __init__(self, profile, *args, **kwargs):
        super(EditFutureRepairForm, self).__init__(*args, **kwargs)
        self.fields['date_of_repair'].widget = SelectDateWidget()
        self.fields['technician'].queryset = Technician.objects.filter(profile=profile)


class AddRepairForm(ModelForm):
    class Meta:
        model = Repair
        exclude = {'unique_id', 'car'}

    def __init__(self, profile, *args, **kwargs):
        super(AddRepairForm, self).__init__(*args, **kwargs)
        self.fields['date_made'].widget = SelectDateWidget()
        self.fields['technician'].queryset = Technician.objects.filter(profile=profile)


class EditRepairForm(ModelForm):
    class Meta:
        model = Repair
        exclude = {'unique_id', 'car'}

    def __init__(self, profile, *args, **kwargs):
        super(EditRepairForm, self).__init__(*args, **kwargs)
        self.fields['date_made'].widget = SelectDateWidget()
        self.fields['technician'].queryset = Technician.objects.filter(profile=profile)


class AddPhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = {'user'}


class AddEmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = {'user'}


class AddUserAddedInfoForm(ModelForm):
    class Meta:
        model = ProfileAddedInfo
        exclude = {'profile_info'}


class EditUserForm(ModelForm):
    class Meta:
        model = Profile
        labels = {'fname': _('First Name'), 'lname': _('Last Name')}
        exclude = {'user', 'id', 'password'}


class EditUserAddedInfoForm(ModelForm):
    class Meta:
        model = ProfileAddedInfo
        exclude = {'profile_info'}


        # class AddPhoneTimingsForm(ModelForm):
        #     class Meta:
        #         model = PhoneTimings
        #
        # class AddEmailTimingsForm(ModelForm):
        #     class Meta:
        #         model = EmailTimings
