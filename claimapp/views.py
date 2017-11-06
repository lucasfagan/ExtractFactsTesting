# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from .models import Speak
from datetime import datetime, date, timedelta

global searchname
global searchdate
global searchtext
global detailSender
# Create your views here.

def index(request):
    context={}
    #reset the search values
    global searchname
    global searchdate
    global searchtext
    searchname=""
    searchdate=""
    searchtext=""
    return render(request, 'claimapp/index.html', context)
#pass the globals so it shows your most recent search, make it so that it always saves your searches, make table fit and freeze first row, range of dates
def data(request):
    global searchname
    global searchdate
    global searchtext
    global detailSender
    detailSender="data"
    if request.method == 'POST':
        #if something was searched, update the search values
        searchname = request.POST.get('name', None)
        searchdate = request.POST.get('date', None)
        searchtext = request.POST.get('text', None)
    #divide up search into words
    words=[]
    lastspace=-1
    for x in range(0,len(searchtext)):
        if searchtext[x]==" ":
            words.append(searchtext[lastspace+1:x])
            lastspace=x
        if x==len(searchtext)-1:
            words.append(searchtext[lastspace+1:x+1])
    print(words)
    if searchdate!="":
        formatteddate=datetime.strptime(str(searchdate), '%m/%d/%y').date()
        all_data=Speak.objects.filter(speaker__icontains=searchname).filter(date=formatteddate)
        for word in words:
            all_data=all_data.filter(claim__icontains=word)
        all_data=all_data.order_by('-score')
    else:
        all_data=Speak.objects.filter(speaker__icontains=searchname)
        for word in words:
            all_data=all_data.filter(claim__icontains=word)
        all_data=all_data.order_by('-score') #add so that it divides up by words and matches

    context={'data':formatdata(all_data)[:50]}
    return render(request, 'claimapp/data.html', context)

def staticpage(request, selected_page):
    #make this less manuaol!!!
    global detailSender
    detailSender="static"
    if selected_page=="donald-trump":
        all_data=Speak.objects.filter(speaker__icontains=selected_page.replace('-',' ')).order_by('-score')[:10]
    elif selected_page=="tax-policy":
        all_data=Speak.objects.filter(claim__icontains="tax").order_by('-score')[:10]
    elif selected_page=="health-care":
        all_data=Speak.objects.filter(claim__icontains=selected_page.replace("-",' ')).order_by('-score')[:10]
    context={}
    context['category']=selected_page.replace('-',' ').title()
    context['data']=formatdata(all_data)
    return render(request, 'claimapp/data.html', context)

def daily(request):
    global detailSender
    detailSender="daily"
    numbertoshow=10 #number of claims to show for every day
    today=date(2017,10,20)  #datetime.date.today
    week=[today,today-timedelta(days=1),today-timedelta(days=2),today-timedelta(days=3),today-timedelta(days=4),today-timedelta(days=5),today-timedelta(days=6)]
    context={}
    context["numbertoshow"]=numbertoshow
    for x in range(0,7):
        name='day'+str(x+1)
        context[name]=Speak.objects.filter(date=week[x]).order_by('-score')
        context[name]=context[name][:10]
        context[name+'title']=f'{week[x]:%b %d, %Y}'
        for item in context[name]:
            item.speaker=item.speaker.title()
        #day 1 is today, day 7 is 6 days ago completing the week
    return render(request, 'claimapp/daily.html', context)

def detail(request, selected_claim):
    claim=get_object_or_404(Speak, claim_id__exact=selected_claim)
    buttontext=""
    if detailSender=="daily":
        buttontext="Return to daily"
    elif detailSender=="data":
        buttontext="Return to data"
    elif detailSender=="static":
        buttontext="Return to page"
    else:
        buttontext="Return"
    claim.speaker=claim.speaker.title()
    if claim.speaker[len(claim.speaker)-1]==" ":
        claim.speaker=claim.speaker[:len(claim.speaker)-1]
    context={"claim":claim,"buttontext":buttontext,"transcriptlink":"http://www.cnn.com/TRANSCRIPTS/"+claim.trans_id+".html"}
    return render(request, 'claimapp/detail.html', context)

def formatdata(data):
    for item in data:
        item.speaker=item.speaker.title()
        item.score=round(float(item.score),2)

    return data #--change here, take out [] and () in claims (which are speakers)
