from django.contrib import admin
from django.urls import path
from women.views import *
from rest_framework import routers
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women_list', WomenViewSet.as_view({'get': 'list'})),
    path('api/v1/women_list/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

]
