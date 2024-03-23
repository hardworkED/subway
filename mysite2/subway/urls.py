from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'outlets', views.OutletViewSet)

app_name = 'subway'
urlpatterns = [
    path('', views.index, name='index'),
    path('outletlist', views.outletlist, name='outletlist'),
    path('outletlist/<int:id>/', views.detail, name='detail'),
    path('map', views.map, name='map'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]