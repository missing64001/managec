from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import time
import json
from django.db.models import Count,Sum
from django.db import connection, transaction

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


    # Play.objects.create()

    # aa = Play.objects.filter().extra({'day':"Extract(day from date_add(create_time, interval 8 hour) )",
    #                                   'year':"Extract(year from date_add(create_time, interval 8 hour) )",
    #                                   'month':"Extract(month from date_add(create_time, interval 8 hour) )",
    #                                   'sec':"UNIX_TIMESTAMP(finished_time) - UNIX_TIMESTAMP(create_time)",
    #     }).values_list('year','month','day','sec')
    # print(aa.query)
    cursor = connection.cursor()
    playsql = '''select date ,sum(sec) as totle from 
    (select sec,CONCAT(year,'-',LPAD(month, 2, 0),'-',LPAD(day, 2, 0)) as date from(SELECT 
        (Extract(year from date_add(create_time, interval 8 hour) )) AS `year`, 
        (Extract(month from date_add(create_time, interval 8 hour) )) AS `month`, 
        (UNIX_TIMESTAMP(finished_time) - UNIX_TIMESTAMP(create_time)) AS `sec`,
        (Extract(day from date_add(create_time, interval 8 hour) )) AS `day` 
        FROM `yuyu_play`) as t1) as t2
        group by date order by date
        ;'''
    
    cursor.execute(playsql)
    rows = cursor.fetchall()

    da1 = []
    da2 = []
    da3 = []
    for row in rows:
        da1.append(row[0])
        da2.append(24 if float(row[1]/3600) > 24 else float(row[1]/3600))
        da3.append(2)
    data.update({'date':json.dumps(da1),
        'data1':json.dumps(da2),
        'data2':json.dumps(da3),
    })

    return render(request,'System_analysis2.html',data)

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


    

