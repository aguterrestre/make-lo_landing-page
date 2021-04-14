from django.urls import path

from core.page import views

app_name = 'page'

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
]
