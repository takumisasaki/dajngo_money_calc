from django.contrib import admin
from django.urls import path
from .views import signupfunk, loginfunk, logoutfunk, toppagefunk, MoneyCreate, moneylistfunk, moneyupdatefunk, MoneyUpdate, logoutfunk

urlpatterns = [
    path('toppage/', toppagefunk, name='toppage'),
    path('signup/', signupfunk, name='signup'),
    path('login/', loginfunk, name='login'),
    path('logout', logoutfunk, name='logout'),
    path('moneycreate/', MoneyCreate.as_view(), name='moneycreate'),
    path('moneylist/<int:pk>', moneylistfunk, name='moneylist'),
    path('moneyupdate/<int:pk>', MoneyUpdate.as_view(), name='moneyupdate')
]
