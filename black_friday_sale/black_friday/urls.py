from django.contrib import  admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from black_friday import views
from django.views.generic.base import RedirectView
router = routers.DefaultRouter()
router.register(r'black_friday',views.PriceView)

urlpatterns = [
    url(r'^api/',include(router.urls)),
    path('',RedirectView.as_view(url='api/'))
]