from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("polling_unit/<int:pu_unique_id>/results", views.get_pu_result, name="polling_unit_results"),
    path("lga/", views.get_lga, name="lga"),
    path("lga/results", views.get_lga_result, name="lga_result"),
    path("new_polling_unit", views.new_polling_unit, name="new_polling_unit"),
    path("views.create_polling_unit", views.create_polling_unit, name="create_polling_unit"),
]
