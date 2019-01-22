import json
from django.shortcuts import render
from .models import MentenanceMaster
from .models import CarReservationMaster
import datetime
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
            event_sub_arr['title'] = i.CarName
            start_date = datetime.datetime.strptime(str(i.StartDateTime.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.EndDateTime.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['description'] = i.MentenanceOverview
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":Mente_events,
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