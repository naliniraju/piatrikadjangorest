DjangoRestFramework Setup
=========================
install python latest stabilized version with pip(>=3.5)

Create mysqldatabasename as piatrikadb

mkdir piatrikadjangorest
cd piatrikadjangorest
virtualenv env

source env/Scripts/activate

(env)---like this will appear in commandprompt once u activated.

pip install django
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient

django-admin startproject piatrikadjangorest
django-admin startapp plots
[[[[[[[[[[[[[[[[=======================Settings file==================================]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
settings.py add below
======================
    # Django REST framework 
    'rest_framework',
    # Customers application 
    'plots.apps.PlotsConfig',
    #cors
    'corsheaders',
	
middileware add below code
==========================
 # CORS
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',
	
above TEMPLATES add below code
==============================
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
)
Change database like below
==========================
DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'piatrikadb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    }
}
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[=============================SETTINGS file End===========================]]]]]]]]]]]]]]
goto models.py in and add
from django.db import models
from datetime import date
# Create your Plot models here.

class Plot(models.Model):
    season=models.CharField(max_length=70, blank=False, default='')
    csi=models.CharField(max_length=70, blank=False, default='')
    section=models.CharField(max_length=70, blank=False, default='')
    offerno=models.CharField(max_length=70, blank=False, default='')
    offerdate=models.DateField(blank=True,null=True)
    planteddate=models.DateField(blank=True,null=True)
    plottype=models.CharField(max_length=70, blank=False, default='')
    plotno=models.CharField(max_length=70, blank=False, default='')
    ryot=models.CharField(max_length=70, blank=False, default='')
    village=models.CharField(max_length=70, blank=False, default='')
    rationtype=models.CharField(max_length=70, blank=False, default='')
    agreementacre=models.CharField(max_length=70, blank=False, default='')
    agreementedtonne=models.CharField(max_length=70, blank=False, default='')
    measuredarea=models.CharField(max_length=70, blank=False, default='')
    guarantor1=models.CharField(max_length=70, blank=False, default='')
    guarantor2=models.CharField(max_length=70, blank=False, default='')
    guarantorname=models.CharField(max_length=70, blank=False, default='')

    

# Create your Ryot models here.
class Ryot(models.Model):
    ryotcode=models.CharField(max_length=70, blank=False, default='')
    ryotname=models.CharField(max_length=70, blank=False, default='')
    grouprefno=models.CharField(max_length=70, blank=False, default='')
    fwgname=models.CharField(max_length=70, blank=False, default='')
    villagecode=models.CharField(max_length=70, blank=False, default='')
    villagename=models.CharField(max_length=70, blank=False, default='')
    mandalcode=models.CharField(max_length=70, blank=False, default='')
    mandalname=models.CharField(max_length=70, blank=False, default='')
    csicode=models.CharField(max_length=70, blank=False, default='')
    csiname=models.CharField(max_length=70, blank=False, default='')
    sectioncode=models.CharField(max_length=70, blank=False, default='')
    sectionname=models.CharField(max_length=70, blank=False, default='')
    literarystatus=models.CharField(max_length=70, blank=False, default='')
    email=models.CharField(max_length=70, blank=False, default='')
    address1=models.CharField(max_length=70, blank=False, default='')
    address2=models.CharField(max_length=70, blank=False, default='')
    city=models.CharField(max_length=70, blank=False, default='')
    paymode=models.CharField(max_length=70, blank=False, default='')
    landno=models.CharField(max_length=70, blank=False, default='')
    mobileno=models.CharField(max_length=70, blank=False, default='')
    bankcode=models.CharField(max_length=70, blank=False, default='')
    bankname=models.CharField(max_length=70, blank=False, default='')
    sbacno=models.CharField(max_length=70, blank=False, default='')
    loanacno=models.CharField(max_length=70, blank=False, default='')
    ledgerno=models.CharField(max_length=70, blank=False, default='')
    loanaccountledgerno=models.CharField(max_length=70, blank=False, default='')
    foliono=models.CharField(max_length=70, blank=False, default='')
    loanacfoliono=models.CharField(max_length=70, blank=False, default='')



========================================================

goto envirinment commandprompt enter

python manage.py makemigrations

python manage.py migrate


=======================================================

======================================

create serilaizers.py in plots
================================
from rest_framework import serializers
from plots.models import Plot
from plots.models import Ryot


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ('id', 'season', 'csi', 'section', 'offerno', 'offerdate',
                  'planteddate', 'plottype', 'plotno', 'ryot', 'village',
                  'rationtype', 'agreementacre', 'agreementedtonne',
                  'measuredarea', 'guarantor1', 'guarantor2', 'guarantorname')


class RyotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ryot
        fields = ('id', 'ryotcode', 'ryotname', 'grouprefno', 'fwgname',
                  'villagecode', 'villagename', 'mandalcode', 'mandalname',
                  'csicode', 'csiname', 'sectioncode', 'sectionname',
                  'literarystatus', 'email', 'address1', 'address2', 'city',
                  'paymode', 'landno', 'mobileno', 'bankcode', 'bankname',
                  'sbacno', 'loanacno', 'ledgerno', 'loanaccountledgerno',
                  'foliono', 'loanacfoliono')
=================================================================
plots/urls.py
=====================================
from django.conf.urls import url 
from plots import views 
 
urlpatterns = [ 
    url(r'^plots/$', views.master),
    url(r'^plots/(?P<pk>[0-9]+)$', views.master_detail),
    url(r'^ryots/$', views.master),
    url(r'^ryots/(?P<pk>[0-9]+)$', views.master_detail),
]

piatrikadjangorest/urls.py
==================================
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('plots.urls')),
]
========================================
plots/views.py
===============
from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from plots.models import Plot,Ryot
from plots.serializers import PlotSerializer,RyotSerializer
 
 
@csrf_exempt
def master(request):
    if request.method == 'GET':
        plots,Ryot = Plot.objects.all()
        plots_serializer = PlotSerializer(plots,ryots, many=True)
        return JsonResponse(plots_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        plot_data = JSONParser().parse(request)
        plot_serializer = PlotSerializer(data=plot_data)
        if plot_serializer.is_valid():
            plot_serializer.save()
            return JsonResponse(plot_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(plot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
 
@csrf_exempt 
def master_detail(request, pk):
    try: 
        plot = Plot.objects.get(pk=pk) 
    except Plot.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        plot_serializer = PlotSerializer(plot) 
        return JsonResponse(plot_serializer.data) 
 
   
 
    
=============================================================

goto environment commandpromp createsuperuser to access admin
==============================================================
winpty python manage.py createsuperuser

finally run

python manage.py runserver

then after check browser http://localhost:8000/plots/

then ng serve -o and check http://localhost:4200
===========================================================================
IMPORTANT NOTICE: Angular services api url should be http://localhost:8000
===========================================================================




