from django.shortcuts import render
from .models import Truck, Model

def overload_info(trucks):
    info = []
    for truck in trucks:
        overload = 0
        if truck.curr_load > truck.model.max_tonnage:
            overload = round(((truck.curr_load/truck.model.max_tonnage - 1) * 100), 1)
        info.append([truck, overload])
    return info

def table(request):

    models = Model.objects.all()

    if request.method == "POST":
        select = request.POST['select']

        if select == 'Все':
            trucks = Truck.objects.all()
        else:
            trucks = Truck.objects.filter(model__name = select)

    else:
        trucks = Truck.objects.all()

    return render(request, 'infotable/table.html', {'info' : overload_info(trucks), 'models' : models})

