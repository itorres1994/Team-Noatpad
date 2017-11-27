from django.shortcuts import render
from .models import Car, User, Technician, FutureRepair, PhoneTimings, EmailTimings, Notifications, Repair

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AddTechnicianForm, AddTechAddedInfoForm, AddCarForm, AddFutureRepairForm, AddRepairForm, AddPhoneForm, AddEmailForm, AddUserAddedInfoForm

import datetime


# Create your views here.
def index(request):
    user = User.objects.all()[0]
    cars = Car.objects.all()
    techs = Technician.objects.all()
    # future_repairs = FutureRepair.objects.all()
    # user_added_info = User.info.all()
    return render(
        request,
        'index.html',
        context={
            'user': user, 'cars': cars, 'techs': techs,
            # 'future_repairs': future_repairs,
        },
    )


def car_prof(request, unique_id):
    num_users = User.objects.all().count()
    cars = Car.objects.all()
    car = Car.objects.get(unique_id=unique_id)
    techs = Technician.objects.all()
    future_repairs = FutureRepair.objects.all()
    return render(
        request,
        'car.html',
        context={
            'num_users': num_users, 'cars': cars, 'techs': techs,
            'future_repairs': future_repairs, 'car': car,
        },
    )


def tech_prof(request, unique_id):
    num_users = User.objects.all().count()
    cars = Car.objects.all()
    tech = Technician.objects.get(unique_id=unique_id)
    reps = Repair.objects.filter(technician=tech)
    car_set = list(set((c, rep) for c in cars for rep in reps if c.unique_id == rep.car.unique_id))
    car_tech = dict()
    for c, r in car_set:
        if c in car_tech and r not in car_tech[c]:
            car_tech[c].append(r)
        else:
            car_tech[c] = [r]
    techs = Technician.objects.all()
    future_repairs = FutureRepair.objects.all()
    return render(
        request,
        'tech.html',
        context={
            'num_users': num_users, 'cars': cars, 'techs': techs,
            'future_repairs': future_repairs, 'tech': tech,
            'reps': reps, 'car_tech': car_tech,
        },
    )


def stats(request, unique_id):
    num_users = User.objects.all().count()
    cars = Car.objects.all()
    car = Car.objects.get(unique_id=unique_id)
    reps = Repair.objects.all()
    techs = Technician.objects.all()
    future_repairs = FutureRepair.objects.all()
    return render(
        request,
        'stat.html',
        context={
            'num_users': num_users, 'cars': cars, 'techs': techs,
            'future_repairs': future_repairs, 'car': car,
            'reps': reps,
        },
    )


def setting(request):
    cars = Car.objects.all()
    techs = Technician.objects.all()
    phone_timings = PhoneTimings.objects.all()
    email_timings = EmailTimings.objects.all()
    notifications = Notifications.objects.all()
    # note_phone = [(note, pt.phone) for pt in phone_timings for note in pt.notification]
    return render(
        request,
        'settings.html',
        context={
            'cars': cars, 'techs': techs,
            'phone_timings': phone_timings, 'email_timings': email_timings,
            'notifications': notifications,
        }
    )

##### Views for Forms

def add_technician(request, unique_id):
    """
    View function for adding a Technician
    """

    tech_inst=get_object_or_404(Technician, unique_id = unique_id)

    if request.method == 'POST':

        form = AddTechnicianForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            tech_inst.fname = form.cleaned_data['fname']
            tech_inst.lname = form.cleaned_data['lname']
            tech_inst.street = form.cleaned_data['street']
            tech_inst.city = form.cleaned_data['city']
            tech_inst.company = form.cleaned_data['company']

            tech_inst.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = AddTechnicianForm

    return render(request, 'add_technician.html', {'form': form, 'techinst':tech_inst})

def add_technician_info(request, unique_id):
   """
   View function for adding technician info
   """

   techinfo_inst=get_object_or_404(TechAddedInfo, unique_id = unique_id)

   if request.method == 'POST':

       form = AddTechAddedInfoForm(request.POST)

       if form.is_valid():
           # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
           tech_inst.due_back = form.cleaned_data['']
           book_inst.save()

           # redirect to a new URL:
           return HttpResponseRedirect(reverse('all-borrowed') )

   # If this is a GET (or any other method) create the default form.
   else:
       form = AddTechAddedInfoForm()

   return render(request, 'add_technician_info.html', {'form': form, 'techinfo_inst':techinfo_inst})

def add_car(request, unique_id):
   """
   View function for adding a Car
   """

   car_inst=get_object_or_404(Car, unique_id = unique_id)

   if request.method == 'POST':

       form = AddCarForm(request.POST)

       if form.is_valid():
           # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
           car_inst.make = form.cleaned_data['make']
           car_inst.year = form.cleaned_data['year']

           car_inst.save()
           # redirect to a new URL:
           return HttpResponseRedirect(reverse('all-borrowed') )

   # If this is a GET (or any other method) create the default form.
   else:
       form = AddCarForm()

   return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

#def add_future_repair(request, unique_id):
#    """
#    View function for adding Future Repairs
#    """
#
#    future_repairs_inst=get_object_or_404(FutureRepair, unique_id = unique_id)
#
#    if request.method == 'POST':
#
#        form = AddFutureRepairForm(request.POST)
#
#        if form.is_valid():
#            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            tech_inst.due_back = form.cleaned_data['renewal_date']
#            book_inst.save()
#
#            # redirect to a new URL:
#            return HttpResponseRedirect(reverse('all-borrowed') )
#
#    # If this is a GET (or any other method) create the default form.
#    else:
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
#
#    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
#
#def add_repair(request, unique_id):
#    """
#    View function for adding a repair
#    """
#
#    repair_inst=get_object_or_404(Repair, unique_id = unique_id)
#
#    if request.method == 'POST':
#
#        form = AddRepairForm(request.POST)
#
#        if form.is_valid():
#            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            tech_inst.due_back = form.cleaned_data['renewal_date']
#            book_inst.save()
#
#            # redirect to a new URL:
#            return HttpResponseRedirect(reverse('all-borrowed') )
#
#    # If this is a GET (or any other method) create the default form.
#    else:
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
#
#    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
#
#def add_phone(request, unique_id):
#    """
#    View function for adding a phone number
#    """
#
#    phone_inst=get_object_or_404(Phone, unique_id = unique_id)
#
#    if request.method == 'POST':
#
#        form = AddPhoneForm(request.POST)
#
#        if form.is_valid():
#            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            tech_inst.due_back = form.cleaned_data['renewal_date']
#            book_inst.save()
#
#            # redirect to a new URL:
#            return HttpResponseRedirect(reverse('all-borrowed') )
#
#    # If this is a GET (or any other method) create the default form.
#    else:
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
#
#    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
#
#def add_email(request, unique_id):
#    """
#    View function for adding an email
#    """
#
#    email_inst=get_object_or_404(Email, unique_id = unique_id)
#
#    if request.method == 'POST':
#
#        form = AddEmailForm(request.POST)
#
#        if form.is_valid():
#            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            tech_inst.due_back = form.cleaned_data['renewal_date']
#            book_inst.save()
#
#            # redirect to a new URL:
#            return HttpResponseRedirect(reverse('all-borrowed') )
#
#    # If this is a GET (or any other method) create the default form.
#    else:
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
#
#    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
#
#def add_user_info(request, unique_id):
#    """
#    View function for adding User Info
#    """
#
#    userinfo_inst=get_object_or_404(UserAddedInfo, unique_id = unique_id)
#
#    if request.method == 'POST':
#
#        form = AddUserAddedInfoForm(request.POST)
#
#        if form.is_valid():
#            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            tech_inst.due_back = form.cleaned_data['renewal_date']
#            book_inst.save()
#
#            # redirect to a new URL:
#            return HttpResponseRedirect(reverse('all-borrowed') )
#
#    # If this is a GET (or any other method) create the default form.
#    else:
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
#
#    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
#
