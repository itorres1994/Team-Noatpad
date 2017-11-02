from django.shortcuts import render
from .models import Car, User, Technician, FutureRepair, UserAddedInfo, Repair


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
    reps = Repair.objects.all()
    techs = Technician.objects.all()
    future_repairs = FutureRepair.objects.all()
    return render(
        request,
        'tech.html',
        context={
            'num_users': num_users, 'cars': cars, 'techs': techs,
            'future_repairs': future_repairs, 'tech': tech,
            'reps': reps,
        },
    )

