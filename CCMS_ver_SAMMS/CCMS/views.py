from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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