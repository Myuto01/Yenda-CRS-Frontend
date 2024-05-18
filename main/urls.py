from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("login/", views.login_view, name="login" ),
    path("register/", views.register_view, name="register" ),
    path('trip-create/', views.trip_create_view, name="trip-create-view"),
    path("trip-schedule/", views.trip_schedule_view, name="trip-schedule"),

    #bus Urls
    path("bus-list/", views.bus_list_view, name="bus-list"),
    path("create-bus/", views.create_bus_view, name="create-bus"),
    path("edit-bus/", views.edit_bus_view, name="edit-bus"),

    #Driver Urls
    path("create-driver/", views.create_driver_details_view, name="create-driver"),
    path("driver-details/", views.driver_details_view, name="driver-details"),
    path("driver-list/", views.driver_list_view, name="driver-list"),

    #New Order Urls
    path("new-order/", views.new_order_view, name="new-order"),
    path("order-list/", views.order_list_view, name="order-list"),

    #Qr Code Scanner
    path("qrcode-scanner/", views.qr_code_scanner_view, name="qrcode-scanner"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)