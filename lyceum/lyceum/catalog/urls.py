from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.Converter, "date")

app_name = 'catalog'
urlpatterns = [
    path("", views.item_list, name='item_list'),
    path("<int:pk>/", views.item_detail, name='item_detail'),
    path("<date:dt>/<int:pk>/", views.item_data_detail),
    re_path(r"re/(?P<pk>[1-9]\d*)/$", views.item_detail, name='item_detail'),
]
