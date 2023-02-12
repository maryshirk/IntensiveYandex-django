from django.urls import path, register_converter, re_path

from . import converters, views

register_converter(converters.DateConverter, "date")

urlpatterns = [
    path("", views.item_list),
    path("<int:pk>/", views.item_detail),
    re_path(r"re/(?P<pk>[1-9]\d*)/$", views.item_detail),
    path("<date:dt>/<int:pk>/", views.item_data_detail),
]
