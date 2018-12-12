from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import employee_master
from django.http import HttpResponse
from .forms import FriendForm
from .models import Friend
from django.shortcuts import redirect
import calendar
from collections import deque
import datetime

@login_required
def index(request):
    params = {
        'title':'CCMS ver.SAMMS',
        }
    return render(request, 'CCMS/index.html', params)




def add(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/CCMS')
    params = {
        'title': 'Add',
        'form': FriendForm(),
        }
    return render(request, 'CCMS/add.html', params)

def carender(request):
     params = {
        'title':'ここにカレンダーを作ります',
        }
     return render(request, 'CCMS/carender.html',params)
 
 
 