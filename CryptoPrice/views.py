from django.http.response import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect, render

from bitcoin.models import Hour,Day,Week,Month,Year
from .forms import CryptoForm


class CryptoHome(DetailView):
    model=Hour
    template_name='home.html'
    
    def get(self,*args,**kwargs):
        form=CryptoForm()
        h=Hour.objects.all()      
        return render(self.request,"home.html",{'form':form,'h':h})

    def post(self,*args,**kwargs):
        print("2")
        context={}
        form=CryptoForm()
        context['form']=form
        
        if self.request.method=='POST':
            form=CryptoForm(self.request.POST)
            if form.is_valid():
                if(form.cleaned_data['crypto']=='1'):
                    return redirect('bitcoin:bhome')
        return render(self.request,"home.html",context)


class HourView(APIView):
    def get(self,request,format=None):
        p=Hour.objects.values('Prices')
        t=Hour.objects.values('time')
        prices=[]
        date_time=[]
        for c in p:
            prices.append(c['Prices'])
        for k in t:
            date_time.append(k['time'])
        data={
            'x': prices,
            'y': date_time
        }
        return Response(data)

class DayView(APIView):
    def get(self,request,format=None):
        p=Day.objects.values('Prices')
        t=Day.objects.values('time')
        prices=[]
        date_time=[]
        for c in p:
            prices.append(c['Prices'])
        for k in t:
            date_time.append(k['time'])
        data={
            'x': prices,
            'y': date_time
        }
        return Response(data)

class WeekView(APIView):
    def get(self,request,format=None):
        p=Week.objects.values('Prices')
        t=Week.objects.values('time')
        prices=[]
        date_time=[]
        for c in p:
            prices.append(c['Prices'])
        for k in t:
            date_time.append(k['time'])
        data={
            'x': prices,
            'y': date_time
        }
        return Response(data)



class MonthView(APIView):
    def get(self,request,format=None):
            
        p=Month.objects.values('Prices')
        t=Month.objects.values('time')
        prices=[]
        date_time=[]
        for c in p:
            prices.append(c['Prices'])
        for k in t:
            date_time.append(k['time'])
        data={
            'x': prices,
            'y': date_time
        }
        return Response(data)

class YearView(APIView):
    def get(self,request,format=None):
            
        p=Year.objects.values('Prices')
        t=Year.objects.values('time')
        prices=[]
        date_time=[]
        for c in p:
            prices.append(c['Prices'])
        for k in t:
            date_time.append(k['time'])
        data={
            'x': prices,
            'y': date_time
        }
        return Response(data)
