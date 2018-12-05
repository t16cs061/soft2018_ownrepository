from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import employee_master
from django.http import HttpResponse

@login_required
def index(request):
    params = {
        'title':'CCMS-ver.SAMMS',
        'msg':'メインメニュー',
        }
    return render(request, 'CCMS/index.html', params)