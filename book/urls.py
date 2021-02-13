from django.contrib import admin
from django.urls import path
from .views import signupfunk, loginfunk, logoutfunk, toppagefunk, MoneyCreate, moneylistfunk,  MoneyUpdate, logoutfunk, MoneyDelete, moneyeditfunk

urlpatterns = [
    path('toppage/', toppagefunk, name='toppage'),
    path('signup/', signupfunk, name='signup'),
    path('login/', loginfunk, name='login'),
    path('logout', logoutfunk, name='logout'),
    path('moneylist/<int:pk>', moneylistfunk, name='moneylist'),
    path('moneycreate/', MoneyCreate.as_view(), name='moneycreate'),
    path('moneyupdate/<int:pk>', MoneyUpdate.as_view(), name='moneyupdate'),
    path('moneydelete/<int:pk>', MoneyDelete.as_view(), name='moneydelete'),
    path('moneyedit/<int:pk>', moneyeditfunk, name='moneyedit')
]
