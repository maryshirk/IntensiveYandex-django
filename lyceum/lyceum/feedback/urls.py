from django.urls import path

from feedback import views


app_name = 'feedback'

urlpatterns = [
    path('', views.FeedbackView.as_view(), name='feedback'),
    path('thanks/', views.redirect_thanks, name='thanks'),
]
