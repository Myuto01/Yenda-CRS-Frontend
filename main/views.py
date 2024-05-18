from django.shortcuts import render

def register_view(request):
    return render(request, '../templates/registration/registration.html')
    
def login_view(request):
    return render(request, '../templates/registration/login.html')

def dashboard_view(request):
    return render(request, '../templates/dashboard.html')

def trip_create_view(request):
    return render(request, '../templates/trip schedule/create_trip.html')
    
def trip_schedule_view(request):
    return render(request, '../templates/trip schedule/trip_schedule.html')


def trip_schedule_view(request):
    return render(request, '../templates/trip schedule/trip_schedule.html')

#Bus Views 

def bus_list_view(request):
    return render(request, '../templates/buses/bus_list.html')

def create_bus_view(request):
    return render(request, '../templates/buses/create_bus.html')

def edit_bus_view(request):
    return render(request, '../templates/buses/edit_bus.html')


#Driver Views
def create_driver_details_view(request):
    return render(request, '../templates/driver/create_driver_details.html')

def driver_details_view(request):
    return render(request, '../templates/driver/driver_details.html')

def driver_list_view(request):
    return render(request, '../templates/driver/driver_list.html')

# New Order Views
def new_order_view(request):
    return render(request, '../templates/new order/new_order.html')

def order_list_view(request):
    return render(request, '../templates/new order/order_list.html')

#Qr Code Scanner
def qr_code_scanner_view(request):
    return render(request, '../templates/qr_code_scanner/qr_code_scanner.html')