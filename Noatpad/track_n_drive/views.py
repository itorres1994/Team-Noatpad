from django.shortcuts import render
from .models import Car, User, Technician, FutureRepair, PhoneTimings, EmailTimings, Notifications, Repair


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
