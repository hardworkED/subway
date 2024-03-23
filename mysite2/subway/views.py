from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework import viewsets
from .serializers import OutletSerializer
from .models import Outlet


def index(request):
    context = {
    }
    return render(request, 'subway/index.html', context)

def outletlist(request):
    locs = Outlet.objects.all().order_by('name')
    if not locs:
        Outlet.get_data()
        locs = Outlet.objects.all().order_by('name')
    context = {
        'locs': locs,
    }
    return render(request, 'subway/outletlist.html', context)

def detail(request, id):
    outlet = get_object_or_404(Outlet, pk=id)
    return render(request, 'subway/detail.html', {'outlet': outlet})

def map(request):
    context = {
        'key': settings.GOOGLE_API_KEY,
    }
    return render(request, 'subway/map.html', context)


class OutletViewSet(viewsets.ModelViewSet):
    queryset = Outlet.objects.all().order_by('name')
    serializer_class = OutletSerializer