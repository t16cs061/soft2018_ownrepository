from django.shortcuts import render, redirect
from CCMS.models import EmployeeMaster, CarMaster
from .forms import EmployeeForm

# Create your views here.
from django.http import HttpResponse
from django.contrib.admin.filters import ChoicesFieldListFilter
from django.contrib.auth.decorators import login_required

def index(request):
    data = EmployeeMaster.objects.all()
    params = {
        'title':'管理者用画面',
        'form':EmployeeMaster(),
        'data':[],
        }
    if(request.method == 'POST'):
        num = request.POST['id']
        item = EmployeeMaster.objects.get(id=num)
        params['data'] = [item]
        params['form'] = EmployeeForm(request.POST)
    else:
        params['data'] = EmployeeMaster.objects.all()
    
    return render(request, 'ccmsadmin/index.html', params)

def add(request):
    if(request.method == 'POST'):
        obj = EmployeeMaster()
        friend = EmployeeForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/ccmsadmin/index')
    params = {
        'title': 'Add',
        'form': EmployeeForm(),
        }
    return render(request, 'ccmsadmin/add.html', params)

def delete(request,num):
    friend = EmployeeMaster.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/ccmsadmin/index')
    params = {
        'title': 'Delete',
        'id':num,
        'obj': friend,
    }
    return render(request,'ccmsadmin/delete.html',params)

def edit(request, num):
    obj = EmployeeMaster.objects.get(id=num)
    if (request.method == 'POST'):
        friend = EmployeeForm(request.POST, instance=obj)
        friend.save() # レコードを更新
        return redirect(to='/ccmsadmin/index')
    params = {
        'title': 'Edit',
        'id':num,
        'form': EmployeeForm(instance=obj),
    }
    return render(request, 'ccmsadmin/edit.html', params)