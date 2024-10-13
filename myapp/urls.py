from django.contrib import admin
from django.urls import path,include
from myapp.views import person,PersonView,index

from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet) 


urlpatterns = [
   #path("persondata/",person)
   path("data/",index),
]+router.urls
