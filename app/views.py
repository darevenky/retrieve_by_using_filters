from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def dis_topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='cricket')
    #LOT=Topic.objects.get(topic_name='cricket')
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'dis_topic.html',d)


def dis_web(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.filter(url='http://virat.com')
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.filter(name__contains='r')
    LOW=Webpage.objects.filter(name__startswith='v')
    LOW=Webpage.objects.order_by('name')    #names in ascencding order 
    LOW=Webpage.objects.order_by('-name')   #names in descending order
    LOW=Webpage.objects.order_by(Length('name'))  # making order(asc) by Length
    LOW=Webpage.objects.order_by(Length('name').desc())   # making order(desc) by Length
    LOW=Webpage.objects.filter(name__in=('virat','warner'))
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(Q(name='virat') & Q(topic_name='cricket'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')

    d={'web':LOW}
    return render(request,'dis_web.html',d)

def dis_access(request):
    LOA=Access.objects.all()
    LOA=Access.objects.filter(author='ronda')
    LOA=Access.objects.all()[1:3:2]
    LOA=Access.objects.exclude(author='ronda')
    LOA=Access.objects.all()
    LOA=Access.objects.filter(date__gt='2022-08-15')   #gt = greater than(>)
    LOA=Access.objects.filter(date__lt='2022-08-15')   #lt = less than(<)
    LOA=Access.objects.filter(date__gte='2022-08-15')  #gte = greater than equal(<=)
    LOA=Access.objects.filter(date__lte='2022-08-15')  #gte = less than equal(>=)
    LOA=Access.objects.filter(date__month='08')        #fetching exact month in table
    LOA=Access.objects.filter(date__year='2023')          #fetching exact year in table
    LOA=Access.objects.all()
    LOA=Access.objects.filter(date__month__gt='05')    
    LOA=Access.objects.all()

    d={'access':LOA}
    return render(request,'dis_access.html',d)


def update_web(request):

    Webpage.objects.filter(name='virat').update(url='http://kohli.com')
    Webpage.objects.filter(topic_name='cricket').update(name='SRH')
    uw=Topic.objects.get(topic_name='football')
    Webpage.objects.update_or_create(name='messi',defaults={'topic_name':uw},url='http://messi.com')
    OW=Topic.objects.get_or_create(topic_name='chess')[0]
    Webpage.objects.update_or_create(name='anand',defaults={'topic_name':OW},url='http://anand.com')
    Webpage.objects.filter(topic_name='football').delete()
    Webpage.objects.filter(name='dhanchand').delete()
    Webpage.objects.filter(url='http://warner.com').delete()
    Webpage.objects.all().delete()
    d={'web':Webpage.objects.all()}
    return render(request,'dis_web.html',d)