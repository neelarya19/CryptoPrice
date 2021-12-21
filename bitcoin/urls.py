from django.urls import path,include
from . import views

app_name='bitcoin'

urlpatterns = [
    path('',views.PriceHome.as_view(),name='bhome'),
    path('OneHour/',views.PriceHour.as_view(),name='hour'),
    path('OneDay/',views.PriceDay.as_view(),name='day'),
    path('OneWeek/',views.PriceWeek.as_view(),name='week'),
    path('Month/',views.PriceMonth.as_view(),name='month'),
    path('Year/',views.PriceYear.as_view(),name='year'),
    
]