from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils.formats import date_format
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .models import MoneyModel
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
def signupfunk(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'login.html', {'message':'ログインしました'})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザはすでに登録されています'})
    return render(request, 'signup.html')


def loginfunk(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('toppage')
        else:
            return render(request, 'login.html', {'context':'ログインに失敗しました。'})
    return render(request, 'login.html')


def moneylistfunk(request, pk):
    print(pk)
    year = request.POST['year']
    print(year)
    object_list = list(MoneyModel.objects.filter(human_id=pk, year=year).all())
    month1 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('janu', flat=True)
    month1 = (sum(month1))
    month2 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('feb', flat=True)
    month2 = (sum(month2))
    month3 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('mar', flat=True)
    month3 = (sum(month3))
    month4 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('apl', flat=True)
    month4 = (sum(month4))
    month5 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('may', flat=True)
    month5 = (sum(month5))
    month6 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('jun', flat=True)
    month6 = (sum(month6))
    month7 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('jul', flat=True)
    month7 = (sum(month7))
    month8 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('aug', flat=True)
    month8 = (sum(month8))
    month9 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('sep', flat=True)
    month9 = (sum(month9))
    month10 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('octr', flat=True)
    month10 = (sum(month10))
    month11 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('nov', flat=True)
    month11 = (sum(month11))
    month12 = MoneyModel.objects.filter(human_id=pk, year=year).values_list('dec', flat=True)
    month12 = (sum(month12))
    result = [month1, month2, month3, month4, month5, month6, month7, month8,
    month9, month10, month11, month11]
    result = sum(result)

    month_money = [i for i in MoneyModel.objects.filter(human_id=pk, year=year).values('janu', 'feb', 'mar', 'apl', 'may',
        'jun', 'jul', 'aug', 'sep', 'octr', 'nov', 'dec')]
    print(object_list)
    nums = [[int(x) for x in range(1)] for _ in range(len(month_money))]
    for i in range(len(month_money)):
        sums = 0
        for j,l in month_money[i].items():
            sums += l
        nums[i] = sums 
    counter = len(nums)
    return render(request, 'moneylist.html', {
        'nums':nums, 'counter':counter, 'object_list':object_list, 'month1':month1,'month2':month2,'month3':month3,'month4':month4,
        'month5':month5,'month6':month6,'month7':month7,'month8':month8,'month9':month9,'month10':month10,
        'month11':month11,'month12':month12, 'result':result})


def logoutfunk(request):
    logout(request)
    return redirect('login')

@login_required
def toppagefunk(request):
    user = request.user
    # time = request.user.objects.date_joined
    money_year = MoneyModel.objects.filter(human_id=user.id).values_list('year', flat=True)
    money_year = list(set(money_year))
    print(money_year)
    return render(request, 'toppage.html', {'money_year':money_year, 'username':user.username})

def moneyeditfunk(request, pk):
    model = list(MoneyModel.objects.filter(pk=pk).all())
    year = MoneyModel.objects.filter(pk=pk).values_list('year', flat=True)
    return render(request, 'moneyedit.html', {'model':model, 'year':year})

def usereditfunk(request, pk):
    user = User.objects.filter(pk=pk).all()
    return render(request, 'user.html', {'user':user})


class MoneyCreate(LoginRequiredMixin,CreateView):
    template_name = 'moneycreate.html'
    model = MoneyModel
    fields = (
        'human_id', 'year', 'workplace',
        'janu', 'feb', 'mar', 'apl', 'may',
        'jun', 'jul', 'aug', 'sep', 'octr',
        'nov', 'dec'
    )
    success_url = reverse_lazy('toppage')


class MoneyUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'moneyupdate.html'
    model = MoneyModel
    fields = (
        'human_id', 'year', 'workplace',
        'janu', 'feb', 'mar', 'apl', 'may',
        'jun', 'jul', 'aug', 'sep', 'octr',
        'nov', 'dec'
    )
    success_url = reverse_lazy('toppage')

class MoneyDelete(DeleteView):
    template_name = 'moneydelete.html'
    model = MoneyModel
    success_url = reverse_lazy('toppage')
