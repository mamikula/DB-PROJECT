from django.urls import path
from . import views

app_name = 'GdzieTaKeja'
urlpatterns = [
    path('', views.port_list, name="ports"),
    path('ports/', views.port_list, name='ports'),
    path('reservations/',views.reservation,name="reservation"),
    path('<str:port_id>/sectors/',views.sectors,name="sectors"),
    path('<str:port_id>/<str:sector_name>/<int:y_id>/slots/',views.slots,name="slots"),
    path('<str:port_id>/<str:sector_name>/<int:y_id>/<int:slot_id>/reserve',views.reserve,name="reserve"),
    path('<str:reservation_number>/', views.edit_reservation, name="edit_reservation")
    ]



