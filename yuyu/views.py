from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import time
# Create your views here.


def Index(request):
    play = Play.objects.latest('id')
    d1 = play.create_time
    d2 = play.finished_time
    d1 = time.mktime(d1.timetuple())
    d2 = time.mktime(d2.timetuple())
    data = {}
    if d2-d1 < 1:
        timer_id = play.id
        starttime = (d1+28800) * 1000
        data = {'timer_id':timer_id,'starttime':starttime}
        print(data)
    return render(request,'play.html',data)

def OptTimer(request):
    timer_id = request.GET.get('id')
    if timer_id and timer_id != '-1':
        print('----------timer_id----------')
        print(timer_id)
        play = Play.objects.get(id = timer_id)
        lastplay = Play.objects.latest('id')
        if play == lastplay:
            play.save()
            return HttpResponse(str(-1))
        else:
            return HttpResponse('redirect')
    else:
        print('xxxxxxx')
        play = Play()
        play.save()
        print(play.id,play.create_time,play.finished_time)
        return HttpResponse(str(play.id))