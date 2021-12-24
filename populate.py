# from Bitcoin.models import OneDay
#API Secret: K0niH0M0BbqVyqgX90pNoElp55DRaIfm
#API Key: iG8FMQ5sHeiDSPy6
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','CryptoPrice.settings')
import django
django.setup()
from bitcoin.models import Hour,Day,Week,Month,Year
from coinbase.wallet.client import Client
from coinbase.wallet.model import APIObject
from dotenv import load_dotenv
load_dotenv()


# d=client._make_api_object(client._get('v2','prices','BTC-USD','historic'),APIObject)

# price = client.get_spot_price(currency_pair = 'BTC-USD',date="2021-12-02")
# print(price)
#one hour solution
import datetime


# print(c['prices'][0]['time'])
# print(c['prices'][0]['time'][0:4])
# print(c['prices'][0]['time'][5:7])
# print(c['prices'][0]['time'][8:10])
# print(c['prices'][0]['time'][11:13])
# print(c['prices'][0]['time'][14:16])
# print(c['prices'][0]['time'][17:19])

API_KEY=os.environ['API_KEY']
API_SECRET_KEY=os.environ['API_SECRET_KEY']
print("hello")


client = Client(API_KEY,API_SECRET_KEY)

c=client.get_historic_prices(currency_pair='BTC-USD',period='hour')
for x in c['prices']:
    p=x['price']
    d=x['time']
    if((int(d[14:16]))%2==0 and d[17:19]=='00'):
        q=Hour(Prices=p,time=d)
        q.save()

c=client.get_historic_prices(currency_pair='BTC-USD',period='day')
for x in c['prices']:
    p=x['price']
    d=x['time']
    q=Day(Prices=p,time=d)
    q.save()

c=client.get_historic_prices(currency_pair='BTC-USD',period='week')
for x in c['prices']:
    p=x['price']
    d=x['time']
    q=Week(Prices=p,time=d)
    q.save()


c=client.get_historic_prices(currency_pair='BTC-USD',period='month')
for x in c['prices']:
    p=x['price']
    d=x['time']
    q=Month(Prices=p,time=d)
    q.save()

c=client.get_historic_prices(currency_pair='BTC-USD',period='year')
for x in c['prices']:
    p=x['price']
    d=x['time']
    q=Year(Prices=p,time=d)
    q.save()

print("hello")

# price = client.get_spot_price(currency_pair = 'BTC-USD')
# p=price['amount']
# q=SpotPrice(Prices=p)
# q.save()
# b=SpotPrice.objects.filter(id__in=list(SpotPrice.objects.values_list('pk', flat=True)[:1]))
# print(b)
# b.delete()
# print(b)




# price = client.get_spot_price(currency_pair = 'BTC-USD')
# p=price['amount']
# q=SpotPrice(Prices=p)
# q.save()


# c=client.get_historic_prices(currency_pair='BTC-USD',period='hour')
# for x in c['prices']:
#     p=x['price']
#     d=datetime.datetime(int(x['time'][0:4]),int(x['time'][5:7]),int(x['time'][8:10]),int(x['time'][11:13]),int(x['time'][14:16]),int(x['time'][17:19]),0)
#     q=OneHour(Prices=p,time=d)
#     q.save()

# c=client.get_historic_prices(currency_pair='BTC-USD',period='day')
# for x in c['prices']:
#     p=x['price']
#     d=datetime.datetime(int(x['time'][0:4]),int(x['time'][5:7]),int(x['time'][8:10]),int(x['time'][11:13]),int(x['time'][14:16]),int(x['time'][17:19]),0)
#     q=OneDay(Prices=p,time=d)
#     q.save()

# c=client.get_historic_prices(currency_pair='BTC-USD',period='week')
# for x in c['prices']:
#     p=x['price']
#     d=datetime.datetime(int(x['time'][0:4]),int(x['time'][5:7]),int(x['time'][8:10]),int(x['time'][11:13]),int(x['time'][14:16]),int(x['time'][17:19]),0)
#     q=OneWeek(Prices=p,time=d)
#     q.save()



# c=client.get_historic_prices(currency_pair='BTC-USD',period='month')
# for x in c['prices']:
#     p=x['price']
#     d=datetime.datetime(int(x['time'][0:4]),int(x['time'][5:7]),int(x['time'][8:10]),int(x['time'][11:13]),int(x['time'][14:16]),int(x['time'][17:19]),0)
#     q=OneMonth(Prices=p,time=d)
#     q.save()


# c=client.get_historic_prices(currency_pair='BTC-USD',period='year')
# for x in c['prices']:
#     p=x['price']
#     d=datetime.datetime(int(x['time'][0:4]),int(x['time'][5:7]),int(x['time'][8:10]),int(x['time'][11:13]),int(x['time'][14:16]),int(x['time'][17:19]),0)
#     q=OneYear(Prices=p,time=d)
#     q.save()


# # print(p)
# # print(d)
# # b1=OneHour.objects.order_by('time')[:1]
# # OneHour.objects.filter(pk__in=b1).delete()
# q1=SpotPrice(Prices=p)
# q1.save()
# b1=SpotPrice.objects.filter(id__in=list(SpotPrice.objects.values_list('pk', flat=True)[:1]))
# b1.delete()

# b1.delete()
# print(b1)

# p=OneHour.objects.values('Prices')
# t=OneHour.objects.values('time')
# prices=[]
# date_time=[]
# for c in p:
#     prices.append(c['Prices'])
# for k in t:
#     date_time.append(k['time'])
# print(prices)
# print(date_time)










