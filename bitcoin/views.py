# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from . import models


class PriceHome(ListView):
    model=models.Hour
    template_name='bitcoin/spotprice_list.html'
    
class PriceHour(ListView):
    model=models.Hour

class PriceDay(ListView):
    model=models.Day
    
class PriceWeek(ListView):
    model=models.Week

class PriceMonth(ListView):
    model=models.Month

class PriceYear(ListView):
    model=models.Year
