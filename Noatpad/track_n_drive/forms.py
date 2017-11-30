from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

from .models import Technician, TechAddedInfo, Car, FutureRepair, Repair, Phone, Email,  \
    ProfileAddedInfo, EmailTimings, PhoneTimings

#ModelForm automatically includes all fields and help texts, exclude is used to
#specifically exclude those fields, and labels overrides the default labels.
#Any info specified here overrides what is shown on models.py

class AddTechnicianForm(ModelForm):
    class Meta:
        model = Technician
        exclude = { 'unique_id' }
        labels = { 'fname': _('First Name'), 'lname': _('Last Name'),}

class AddTechAddedInfoForm(ModelForm):
    class Meta:
        model = TechAddedInfo
        exclude = { 'tech' }

class AddCarForm(ModelForm):
    class Meta:
        model = Car
        exclude = { 'unique_id', 'profile' }
        help_texts=''

class EditCarForm(ModelForm):
    class Meta:
        model = Car
        exclude = { 'unique_id', 'profile' }

class AddFutureRepairForm(ModelForm):
    class Meta:
        model = FutureRepair
        exclude = { 'unique_id' }

class AddRepairForm(ModelForm):
    class Meta:
        model = Repair
        exclude = { 'unique_id' }

class AddPhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = { 'user' }

class AddEmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = { 'user' }

class AddUserAddedInfoForm(ModelForm):
    class Meta:
        model = ProfileAddedInfo
        exclude = { 'user_info' }

# class AddPhoneTimingsForm(ModelForm):
#     class Meta:
#         model = PhoneTimings
#
# class AddEmailTimingsForm(ModelForm):
#     class Meta:
#         model = EmailTimings