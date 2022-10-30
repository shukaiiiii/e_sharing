from django.urls import path, include
from .views import log, customer, manager, operator
from django.urls import path

app_name = 'e_portal'
urlpatterns = [
    # log
    # path('', log.index, name='index'),
    path('', log.login, name='login'),
    path("main/", log.index, name='index'),
    path("register/", log.register, name='register'),
    path("pwd_reset/", log.pwd_reset, name='pwd_reset'),
    path("error404/", log.Error404, name='error404'),

    # customer
    path("vehicles/", customer.getAvailableVehicles, name='vehicles_list'),
    # 进入details页面执行的
    path("vehicles/<int:vehicles_id>/", customer.getVehicleDetails, name='vehicles_detail'),

    # 在details页面执行，rent a car
    path("rent/<int:vehicles_id>/", customer.rent, name='rent'),

    # customer pay
    path("pay/<int:order_id>/", customer.pay, name='payment'),

    # customer report a broken car
    path("report/<int:order_id>/", customer.report, name='report'),

    # return a car
    path("return/<int:order_id>/", customer.returnVehicle, name='returnVehicle'),
    # rental info page
    path("rents/", customer.rents, name='rents'),

    # operator

    # manager

]
