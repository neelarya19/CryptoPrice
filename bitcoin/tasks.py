from celery import shared_task
import datetime
import os
from bitcoin.models import Hour,Day,Week,Month,Year
from coinbase.wallet.client import Client
from coinbase.wallet.model import APIObject
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY=os.environ['API_KEY']
API_SECRET_KEY=os.environ['API_SECRET_KEY']


@shared_task(bind=True)
def update_price_hour(self):
    client = Client(API_KEY,API_SECRET_KEY)
    c=client.get_historic_prices(currency_pair='BTC-USD',period='hour')
    
    for i in range(12):
        d=c['prices'][i]['time']
        if((int(d[14:16]))%2==0 and d[17:19]=='00'):
            count=i
            break
    p=c['prices'][count]['price']
    d=c['prices'][count]['time']
    print(d)
    print("outer")
    if(d[17:19]=='00'):
        print("hour")
        q1=Hour(Prices=p,time=d)
        q1.save()
        b1=Hour.objects.order_by('time')[:1]
        Hour.objects.filter(pk__in=b1).delete()

    if((int(d[14:16])%5==0 and d[17:19]=='00')):
        print("Day")
        q2=Day(Prices=p,time=d)
        q2.save()
        b2=Day.objects.order_by('time')[:1]
        Day.objects.filter(pk__in=b2).delete()

    if(int(d[14:16])%30==0 and d[17:19]=='00'):
        print("month")
        q3=Week(Prices=p,time=d)
        q3.save()
        b3=Week.objects.order_by('time')[:1]
        Week.objects.filter(pk__in=b3).delete()


    
    if(int(d[11:13])%2==0 and d[14:16]=='00' and (d[17:19])=='00'):

        q4=Month(Prices=p,time=d)
        q4.save()
        b4=Month.objects.order_by('time')[:1]
        Month.objects.filter(pk__in=b4).delete()

    if(d[11:13]=='00' and d[14:16]=='00' and d[17:19]=='00'):
        q5=Year(Prices=p,time=d)
        q5.save()
        b5=Year.objects.order_by('time')[:1]
        Year.objects.filter(pk__in=b5).delete()
