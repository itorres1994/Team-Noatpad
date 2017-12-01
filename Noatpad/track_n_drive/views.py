from django.shortcuts import render
from .models import Car, CarAddedInfo, Profile, Technician, FutureRepair, PhoneTimings, EmailTimings, Notifications, \
    Repair, \
    TechAddedInfo, Phone, Email, ProfileAddedInfo

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from .forms import AddTechnicianForm, AddTechAddedInfoForm, AddCarForm, AddFutureRepairForm, AddRepairForm, \
    AddPhoneForm, AddEmailForm, AddUserAddedInfoForm, EditCarForm, EditUserForm, EditUserAddedInfoForm

import datetime


# Create your views here.
def index(request):
    if not request.user.is_anonymous():
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        user_cars = list(c for c in cars if c.profile == profile)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
        # future_repairs = FutureRepair.objects.all()
        # user_added_info = User.info.all()
        return render(
            request,
            'index.html',
            context={
                'profile': profile, 'cars': user_cars, 'techs': user_techs,
                # 'future_repairs': future_repairs,
            },
        )
    else:
        return render(request, 'registration/login.html')


def car_prof(request, unique_id):
    if not request.user.is_anonymous():
        num_users = Profile.objects.all().count()
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        user_cars = list(c for c in cars if c.profile == profile)
        car = Car.objects.get(unique_id=unique_id)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
        future_repairs = FutureRepair.objects.all()
        return render(
            request,
            'car.html',
            context={
                'num_users': num_users, 'cars': user_cars, 'techs': user_techs,
                'future_repairs': future_repairs, 'car': car,
            },
        )
    else:
        return render(request, 'registration/login.html')


def tech_prof(request, unique_id):
    if not request.user.is_anonymous():
        num_users = Profile.objects.all().count()
        cars = Car.objects.all()
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = list(c for c in cars if c.profile == profile)
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
        user_techs = list(t for t in techs if t.profile == profile)
        future_repairs = FutureRepair.objects.all()
        return render(
            request,
            'tech.html',
            context={
                'num_users': num_users, 'cars': cars, 'techs': user_techs,
                'future_repairs': future_repairs, 'tech': tech,
                'reps': reps, 'car_tech': car_tech,
            },
        )
    else:
        return render(request, 'registration/login.html')


def stats(request, unique_id):
    if not request.user.is_anonymous():
        num_users = Profile.objects.all().count()
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        cars = list(c for c in cars if c.profile == profile)
        car = Car.objects.get(unique_id=unique_id)
        reps = Repair.objects.all()
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
        future_repairs = FutureRepair.objects.all()
        return render(
            request,
            'stat.html',
            context={
                'num_users': num_users, 'cars': cars, 'techs': user_techs,
                'future_repairs': future_repairs, 'car': car,
                'reps': reps,
            },
        )
    else:
        return render(request, 'registration/login.html')


def setting(request):
    if not request.user.is_anonymous():
        cars = Car.objects.all()
        profile = Profile.objects.get(id=request.user.profile.id)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
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
    else:
        return render(request, 'registration/login.html')


##### Views for Forms
def add_technician1(request):
    if not request.user.is_anonymous():
        """
        View function for adding a Technician
        """
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        user_cars = list(c for c in cars if c.profile == profile)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
        tech_inst = Technician()

        if request.method == 'POST':

            form = AddTechnicianForm(request.POST)

            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                tech_inst.fname = form.cleaned_data['fname']
                tech_inst.lname = form.cleaned_data['lname']
                tech_inst.street = form.cleaned_data['street']
                tech_inst.profile = request.user.profile
                tech_inst.city = form.cleaned_data['city']
                tech_inst.company = form.cleaned_data['company']

                tech_inst.save()
                # redirect to a new URL:
                return HttpResponseRedirect(reverse('tech', args=[str(tech_inst.unique_id)]))

        # If this is a GET (or any other method) create the default form.
        else:
            form = AddTechnicianForm()

        return render(request, 'add_technician.html', {'form': form, 'techinst': tech_inst, 'cars': user_cars,
                                                       'techs': user_techs, 'profile': profile})
    else:
        return render(request, 'registration/login.html')


def add_technician2(request, unique_id):
    if not request.user.is_anonymous():
        """
        View function for adding a Technician
        """
        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        user_cars = list(c for c in cars if c.profile == profile)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)
        try:
            tech_inst = get_object_or_404(Technician, unique_id=unique_id)
        except:
            tech_inst = Technician()

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
                return HttpResponseRedirect(reverse('tech', args=[str(unique_id)]))

        # If this is a GET (or any other method) create the default form.
        else:
            form = AddTechnicianForm(initial={'fname': tech_inst.fname, 'lname': tech_inst.lname,
                                              'street': tech_inst.street, 'city': tech_inst.city,
                                              'company': tech_inst.company})

        return render(request, 'add_technician.html', {'form': form, 'techinst': tech_inst, 'cars': user_cars,
                                                       'techs': user_techs, 'profile': profile})
    else:
        return render(request, 'registration/login.html')


def add_technician_info(request, unique_id):
    if not request.user.is_anonymous():
        """
        View function for adding technician info
        """
        try:
            techinfo_inst = get_object_or_404(TechAddedInfo, unique_id=unique_id)
        except:
            techinto_inst = TechAddedInfo()

        if request.method == 'POST':

            form = AddTechAddedInfoForm(request.POST)

            if form.is_valid():
                techinfo_inst.information_name = form.cleaned_data['information_name']
                techinfo_inst.information_contents = form.cleaned_data['information_contents']
                techinfo_inst.save()
                return HttpResponseRedirect(reverse('tech', args=[str(unique_id)]))
        else:
            form = AddTechAddedInfoForm()
        return render(request, 'add_technician_info.html', {'form': form, 'techinfo_inst': techinfo_inst})
    else:
        return render(request, 'registration/login.html')


def add_car_info(request, unique_id):
    """
       View function for adding a Car
       """
    try:
        car_inst = get_object_or_404(Car, unique_id=unique_id)
    except:
        return HttpResponseNotFound('Hey Tim :)')
    try:
        car_info_inst = get_object_or_404(CarAddedInfo, car=car_inst)
    except:
        car_info_inst = CarAddedInfo(car=car_inst)
    # return HttpResponseNotFound('Found it...')

    if request.method == 'POST':

        form = EditCarForm(request.POST)
        if form.is_valid():
            car_info_inst.information_name = form.cleaned_data['information_name']
            car_info_inst.information_contents = form.cleaned_data['information_contents']
            car_info_inst.save()
            return HttpResponseRedirect(reverse('car', args=[str(unique_id)]))

            # If this is a GET (or any other method) create the default form.
    else:
        form = EditCarForm()
    return render(request, 'add_car_info.html', {'form': form, 'car_info_inst': car_info_inst, })


def add_car(request):
    if not request.user.is_anonymous():
        """
       View function for adding a Car
       """

        profile = Profile.objects.get(id=request.user.profile.id)
        cars = Car.objects.all()
        user_cars = list(c for c in cars if c.profile == profile)
        techs = Technician.objects.all()
        user_techs = list(t for t in techs if t.profile == profile)

        car_inst = Car()

        if request.method == 'POST':

            form = AddCarForm(request.POST)
            if form.is_valid():
                car_inst.make = form.cleaned_data['make']
                car_inst.model = form.cleaned_data['model']
                car_inst.profile = request.user.profile
                car_inst.year = form.cleaned_data['year']
                car_inst.profile = request.user.profile
                car_inst.engine_type = form.cleaned_data['engine_type']
                car_inst.mileage = form.cleaned_data['mileage']
                car_inst.oil_type = form.cleaned_data['oil_type']
                car_inst.color = form.cleaned_data['color']
                car_inst.registration = form.cleaned_data['registration']
                car_inst.vin_number = form.cleaned_data['vin_number']
                car_inst.save()
                return HttpResponseRedirect(reverse('car', args=[str(car_inst.unique_id)]))

                # If this is a GET (or any other method) create the default form.
        else:
            form = AddCarForm(initial={'make': car_inst.make, 'model': car_inst.model, 'year': car_inst.year,
                                       'engine_type': car_inst.engine_type, 'mileage': car_inst.mileage,
                                       'oil_type': car_inst.oil_type, 'color': car_inst.color,
                                       'registration': car_inst.registration, 'vin_number': car_inst.vin_number})
        return render(request, 'add_car.html', {'form': form, 'car_inst': car_inst, 'car': car_inst, 'cars': user_cars,
                                                'techs': user_techs, 'profile': profile})
    else:
        return render(request, 'registration/login.html')


def edit_car(request, unique_id):
    if not request.user.is_anonymous():
        """
       View function for adding a Car
       """
        try:
            car_inst = get_object_or_404(Car, unique_id=unique_id)
        except:
            return HttpResponseNotFound('Hey Tim :)')

        if request.method == 'POST':

            form = AddCarForm(request.POST)
            if form.is_valid():
                car_inst.make = form.cleaned_data['make']
                car_inst.model = form.cleaned_data['model']
                car_inst.profile = request.user.profile
                car_inst.year = form.cleaned_data['year']
                car_inst.engine_type = form.cleaned_data['engine_type']
                car_inst.mileage = form.cleaned_data['mileage']
                car_inst.oil_type = form.cleaned_data['oil_type']
                car_inst.color = form.cleaned_data['color']
                car_inst.registration = form.cleaned_data['registration']
                car_inst.vin_number = form.cleaned_data['vin_number']
                car_inst.save()
                # car_info_inst.save()
                return HttpResponseRedirect(reverse('car', args=[str(unique_id)]))

                # If this is a GET (or any other method) create the default form.
        else:
            initial = {
                'make': car_inst.make, 'model': car_inst.model, 'year': car_inst.year,
                'engine_type': car_inst.engine_type, 'mileage': car_inst.mileage,
                'oil_type': car_inst.oil_type, 'color': car_inst.color,
                'registration': car_inst.registration, 'vin_number': car_inst.vin_number
            }
            print(initial)
            form = AddCarForm(initial)
        return render(request, 'add_car.html', {'form': form, 'car': car_inst})
    else:
        return render(request, 'registration/login.html')


def add_future_repair(request, unique_id):
    if not request.user.is_anonymous():
        """
        View function for adding Future Repairs
        """
        try:
            technicians = get_list_or_404(Technician, profile=request.user.profile)
        except:
            return HttpResponseNotFound('no technicians found...')
        future_repairs_inst = FutureRepair()
        car_inst = get_object_or_404(Car, unique_id=unique_id)
        if request.method == 'POST':

            form = AddFutureRepairForm(request.user.profile, request.POST)
            if form.is_valid():
                future_repairs_inst.car = car_inst
                future_repairs_inst.name = form.cleaned_data['name']
                future_repairs_inst.date_of_repair = form.cleaned_data['date_of_repair']
                future_repairs_inst.technician = form.cleaned_data['technician']
                # Add technician, car, and notification, ForeignKey
                future_repairs_inst.save()

                return HttpResponseRedirect(reverse('car', args=[str(unique_id)]))
        else:
            form = AddFutureRepairForm(request.user.profile)

        return render(request, 'add_future_repairs.html', {'form': form, 'future_repairs_inst': future_repairs_inst})
    else:
        return render(request, 'registration/login.html')


def add_user_info(request):
    if not request.user.is_anonymous:
        try:
            profile = Profile.objects.get(id=request.user.profile.id)
            cars = Car.objects.all()
            user_cars = list(c for c in cars if c.profile == profile)
            techs = Technician.objects.all()
            user_techs = list(t for t in techs if t.profile == profile)
            pass
        except:
            return HttpResponseNotFound('hello :)')
        profile = Profile.objects.get(id=request.user.profile.id)
        prof_info_inst = ProfileAddedInfo(profile_info=profile)
        if request.method == 'POST':

            form = AddUserAddedInfoForm(request.POST)
            if form.is_valid():
                prof_info_inst.information_name = form.cleaned_data['information_name']
                prof_info_inst.information_contents = form.cleaned_data['information_contents']
                prof_info_inst.profile_info = profile
                prof_info_inst.save()

                return HttpResponseRedirect(reverse('index'))
        else:
            form = AddUserAddedInfoForm()

        return render(request, 'add_user_info.html', {'form': form, 'prof_info_inst': prof_info_inst,
                                                      'cars': user_cars, 'techs': user_techs,
                                                      'profile': profile})
    else:
        return render(request, 'registration/login.html')


def edit_user(request):
    if not request.user.is_anonymous():
        """
        View function for adding Future Repairs
        """
        try:
            profile = Profile.objects.get(id=request.user.profile.id)
            cars = Car.objects.all()
            user_cars = list(c for c in cars if c.profile == profile)
            techs = Technician.objects.all()
            prof_inst = get_object_or_404(Profile, id=request.user.profile.id)
            # prof_info_inst = get_list_or_404(ProfileAddedInfo, profile_info=prof_inst)
        except:
            return HttpResponseNotFound('hello :)')

        prof_info_ins = get_list_or_404(ProfileAddedInfo, profile_info=prof_inst)
        if request.method == 'POST':

            # form = EditUserForm(request.POST)
            # if form.is_valid():
            prof_inst.fname = request.POST.get('fname')
            prof_inst.lname = request.POST.get('lname')
            prof_inst.save()
            i = 0
            for key, content in request.POST.items():
                if 'name' in key:
                    prof_info_ins.__getitem__(i).information_name = content
                elif 'content' in key:
                    prof_info_ins.__getitem__(i).information_contents = content
                    prof_info_ins.__getitem__(i).save()
                    i += 1

            print(prof_inst)

            return HttpResponseRedirect(reverse('index'))
        # else:
        #     form = EditUserForm(initial={
        #         'fname': prof_inst.fname, 'lname': prof_inst.lname
        #     })

        return render(request, 'edit_user.html', {'prof_inst': prof_inst, 'prof_info_inst': prof_info_ins,
                                                  'cars': user_cars, 'techs': techs})

    else:
        return render(request, 'registration/login.html')

# def add_repair(request, unique_id):
#     """
#     View function for adding a repair
#     """
#     try:
#         repair_inst = get_object_or_404(Repair, unique_id=unique_id)
#     except:
#         tech_inst = Repair()
#
#     if request.method == 'POST':
#
#         form = AddRepairForm(request.POST)
#         if form.is_valid():
#             repair_inst.name = form.cleaned_data['name']
#             repair_inst.cost = form.cleaned_data['cost']
#             repair_inst.date_made = form.cleaned_data['date_made']
#             repair_inst.save()
#
#             return HttpResponseRedirect(reverse('car', args=[str(unique_id)]))
#
#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = AddRepairForm(initial={'renewal_date': proposed_renewal_date, })
#
#     return render(request, 'add_repair.html', {'form': form, 'repair_inst': repair_inst})
#
#
# def add_phone(request, unique_id):
#     """
#     View function for adding a phone number
#     """
#     try:
#         phone_inst = get_object_or_404(Phone, unique_id=unique_id)
#     except:
#         phone_inst = Phone()
#
#     if request.method == 'POST':
#
#         form = AddPhoneForm(request.POST)
#         if form.is_valid():
#             phone_inst.number = form.cleaned_data['number']
#             # add user, ForeignKey
#             phone_inst.save()
#
#             return HttpResponseRedirect(reverse('settings'))
#
#     else:
#
#         form = AddPhoneForm()
#
#     return render(request, 'add_phone.html', {'form': form, 'phone_inst': phone_inst})
#
#
# def add_email(request, unique_id):
#     """
#     View function for adding an email
#     """
#     try:
#         email_inst = get_object_or_404(Email, unique_id=unique_id)
#     except:
#         email_inst = Email()
#
#     if request.method == 'POST':
#
#         form = AddEmailForm(request.POST)
#
#         if form.is_valid():
#             email_inst.address = form.cleaned_data['address']
#             # add user, ForeignKey
#             email_inst.save()
#
#             return HttpResponseRedirect(reverse('settings'))
#
#     else:
#
#         form = AddEmailForm()
#
#     return render(request, 'add_email.html', {'form': form, 'email_inst': email_inst})
#
#
# def add_user_info(request, unique_id):
#     """
#     View function for adding User Info
#     """
#     try:
#         userinfo_inst = get_object_or_404(ProfileAddedInfo, unique_id=unique_id)
#     except:
#         userinfo_inst = ProfileAddedInfo()
#
#     if request.method == 'POST':
#
#         form = AddUserAddedInfoForm(request.POST)
#
#         if form.is_valid():
#             userinfo_inst.information_name = form.cleaned_data['information_name']
#             userinfo_inst.contents = form.cleaned_data['contents']
#             userinfo_inst.save()
#
#             return HttpResponseRedirect(reverse('settings'))
#
#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = AddUserAddedInfoForm()
#     return render(request, 'add_user_info', {'form': form, 'userinfo_inst': userinfo_inst})
