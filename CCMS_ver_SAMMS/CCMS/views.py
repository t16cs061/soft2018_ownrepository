from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FriendForm, MentenanceForm,ServiceRecordForm
from .models import Friend, MentenanceMaster,ServiceRecordMaster
import calendar
from collections import deque
import datetime

from .filters import ServiceRecordFilter 
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

@login_required
def index(request):
    params = {
        'title':'CCMS ver.SAMMS',
        }
    return render(request, 'CCMS/index.html', params)

@login_required
def mentenance(request):
    params = {
        'title':'メンテナンス',
        }
    return render(request, 'CCMS/mentenance/index.html', params)

def mentenance_reserve(request):
    params = {
        'title':'メンテナンス予約',
        }
    return render(request, 'CCMS/mentenance/reserve.html', params)

def mentenance_check(request):
    params = {
        'title':'メンテナンス予約確認',
        }
    return render(request, 'CCMS/mentenance/check.html', params)

def mentenance_add(request):
    if (request.method == 'POST'):
        obj = MentenanceMaster()
        mentenance_detail = MentenanceForm(request.POST, instance=obj)
        mentenance_detail.save
        return redirect(to='/')
    
    params = {
        'title': 'メンテナンス予約フォーム',
        'form': MentenanceForm(),
        }
    return render(request, 'CCMS/mentenance/detail.html', params)

def add(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save
        return redirect(to='/')
    params = {
        'title': '予約フォーム',
        'form': FriendForm(),
        }
    return render(request, 'CCMS/add.html', params)

def carender(request):
    params = {
        'title':'ここにカレンダーを作ります',
        'go':'ニコニコ薬局',
        }
    return render(request, 'CCMS/carender.html',params)

def servicerecord(request):
    
    if (request.method == 'POST'):
        msg = 'Search result:'
        form = ServiceRecordForm(request.POST)
        option_str = request.POST['option']
        search_str = request.POST['search']
        if(search_str == ''):
            data = Friend.objects.all()
        else:    
            if (option_str == 'car_name'): 
                data = Friend.objects.filter(car_name__contains = search_str)
            elif (option_str == 'start_day'):
                data = Friend.objects.filter(star_day__contains = search_str)
            elif (option_str == 'end_day'):
                data = Friend.objects.filter(end_day__contains = search_str)
            elif (option_str == 'want_go'):
                data = Friend.objects.filter(want_go__contains = search_str)
            
    else:
        msg = 'Search'
        form = ServiceRecordForm()
        data = Friend.objects.all()
    params = {
        'title':'運行記録',
        'message':msg,
        'form':form,
        'data': data,
        
    }
    return render(request, 'CCMS/confirmation/t_confirmation.html', params)
def Refuelrecord(request):
    
    if (request.method == 'POST'):
        msg = 'Search result:'
        form = ServiceRecordForm(request.POST)
        option_str = request.POST['option']
        search_str = request.POST['search']
        if(search_str == ''):
            data = Friend.objects.all()
        else:    
            if (option_str == 'car_name'): 
                data = Friend.objects.filter(car_name__contains = search_str)
            elif (option_str == 'start_day'):
                data = Friend.objects.filter(star_day__contains = search_str)
            elif (option_str == 'end_day'):
                data = Friend.objects.filter(end_day__contains = search_str)
            elif (option_str == 'want_go'):
                data = Friend.objects.filter(want_go__contains = search_str)
            
    else:
        msg = 'Search'
        form = ServiceRecordForm()
        data = Friend.objects.all()
    params = {
        'title':'運行記録',
        'message':msg,
        'form':form,
        'data': data,
        
    }
    return render(request, 'CCMS/confirmation/f_confirmation.html', params)
def ETCrecord(request):
    
    if (request.method == 'POST'):
        msg = 'Search result:'
        form = ServiceRecordForm(request.POST)
        option_str = request.POST['option']
        search_str = request.POST['search']
        if(search_str == ''):
            data = Friend.objects.all()
        else:    
            if (option_str == 'car_name'): 
                data = Friend.objects.filter(car_name__contains = search_str)
            elif (option_str == 'start_day'):
                data = Friend.objects.filter(star_day__contains = search_str)
            elif (option_str == 'end_day'):
                data = Friend.objects.filter(end_day__contains = search_str)
            elif (option_str == 'want_go'):
                data = Friend.objects.filter(want_go__contains = search_str)
            
    else:
        msg = 'Search'
        form = ServiceRecordForm()
        data = Friend.objects.all()
    params = {
        'title':'運行記録',
        'message':msg,
        'form':form,
        'data': data,
        
    }
    return render(request, 'CCMS/confirmation/e_confirmation.html', params)