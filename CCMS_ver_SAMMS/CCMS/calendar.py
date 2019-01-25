import json
from django.shortcuts import render
from .models import MentenanceMaster
from .models import CarReservationMaster
import datetime
from django.utils import timezone
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

def get(request):
    Mente_events = MentenanceMaster.objects.all()
    
    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        Mente_events = MentenanceMaster.objects.all()
        
        for i in Mente_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.CarName + ",メンテナンス"
            start_date = datetime.datetime.strptime(str(i.StartDateTime.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            start_hour = datetime.datetime.strptime(str(i.StartDateTime.time()), "%H:%M:%S").strftime("%H:%M:%S")
            end_date = datetime.datetime.strptime(str(i.EndDateTime.date()), '%Y-%m-%d').strftime("%Y-%m-%d")
            end_hour = datetime.datetime.strptime(str(i.EndDateTime.time()), "%H:%M:%S").strftime("%H:%M:%S")
            event_sub_arr['start'] = start_date + " " + start_hour
            event_sub_arr['end'] = end_date + " " + end_hour
            event_sub_arr['allDay'] = i.AllDay
            event_sub_arr['description'] = i.MentenanceOverview
            
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":Mente_events,
    }
    return render(request,'CCMS/mentenance/reserve.html',context) 

#イベント登録用関数
def regist(request):
    if request.POST:
        postdata = json.loads(request.body.decode())
        
        CarName = postdata.get('title', None)
        Start = postdata.get('start', None)
        End = postdata.get('end', None)
        AllDay = postdata.get('allDay', None)
        Description = postdata.get('description', None)
        
        mentenance = MentenanceMaster()
        mentenance.CarName = CarName
        mentenance.StartDateTime = Start
        mentenance.EndDateTime = End
        mentenance.AllDay = AllDay
        mentenance.MentenanceOverview = Description
        mentenance.save()
        
        context = {
            "jsonResponce":"success",
        }
        return render(request,'CCMS/mentenance/reserve.html',context) 
    
def getAdd(request):
    add_events = CarReservationMaster.objects.all()
    
    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        add_events = CarReservationMaster.objects.all()
        
        for i in add_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.CarName
            start_date = datetime.datetime.strptime(str(i.StartDateTime.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.EndDateTime.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['description'] = i.addOverview
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":add_events,
    }
    return render(request,'CCMS/carender.html',context) 