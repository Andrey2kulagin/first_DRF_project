from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth/', include("djoser.urls.authtoken")),
    # path('api/v1/women_list', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/women_list/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

]
