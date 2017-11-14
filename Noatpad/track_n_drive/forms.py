from django import ModelForms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

from .models import Technician, TechAddedInfo, Car, FutureRepair, Repair, Phone, Email, UserAddedInfo

class AddTechnicianForm(ModelForm):
    class Meta:
        model = Technician
        fields = ['fname', 'lname',]
        labels = { 'fname': _('First Name'), 'lname': _('Last Name'),}
        help_texts = { 'fname': _('Enter Technician first name.'),}
