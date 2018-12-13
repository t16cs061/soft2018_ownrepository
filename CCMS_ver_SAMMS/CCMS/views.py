from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FriendForm
from .models import Friend
import calendar
from collections import deque
import datetime


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
  
def add(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/')
    params = {
        'title': '予約フォーム',
        'form': FriendForm(),
        }
    return render(request, 'CCMS/add.html', params)

def carender(request):
     params = {
        'title':'ここにカレンダーを作ります',
        }
     return render(request, 'CCMS/carender.html',params)
 
 