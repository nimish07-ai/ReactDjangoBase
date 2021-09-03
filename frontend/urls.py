from django.contrib import admin
from django.urls import path,include
from  .views import *

urlpatterns = [
    path('',BaseReactfile.as_view(),name="base")
        ]