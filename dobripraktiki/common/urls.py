from django.urls import path

from dobripraktiki.common.views import HomeView, ServicesView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('uslugi/', ServicesView.as_view(), name='services'),
    path('kontakti/', ContactView.as_view(), name='contact'),
]