from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

from .models import Technician, TechAddedInfo, Car, FutureRepair, Repair, Phone, Email,  \
    UserAddedInfo, EmailTimings, PhoneTimings

class AddTechnicianForm(ModelForm):
    class Meta:
        model = Technician
        exclude = { 'unique_id' }
        labels = { 'fname': _('First Name'), 'lname': _('Last Name'),}

class AddTechAddedInfoForm(ModelForm):
    class Meta:
        model = TechAddedInfo

class AddCarForm(ModelForm):
    class Meta:
        model = Car
        exclude = { 'unique_id' }

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

class AddEmailForm(ModelForm):
    class Meta:
        model = Email

class AddUserAddedInfoForm(ModelForm):
    class Meta:
        model = UserAddedInfo

# class AddPhoneTimingsForm(ModelForm):
#     class Meta:
#         model = PhoneTimings
#
# class AddEmailTimingsForm(ModelForm):
#     class Meta:
#         model = EmailTimings