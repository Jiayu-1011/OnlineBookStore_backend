from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *

def setIndex(request):
    return render(request, 'index.html')


@api_view(['POST', 'GET'])
def getTeam(request):
    print(request)
    if request.method == 'POST':
        if request.body:
            req = json.loads(request.body)
            print(req)
        return JsonResponse({
            'team': '辛嘉宇、汪涛、陈炜鹏、文涛、商政淳'
        })

def GETTest(request):
    print(request)
    if request.method == 'GET':

        method = request.GET.get('method');
        print(method)
        if method == 'GET':
            return HttpResponse('GET测试成功');


def POSTTest(request):
    print(request)
    if request.method == 'POST':
        if request.body:
            print(request.body)
            print(request.POST.get('method'))
            return HttpResponse('POST接口测试成功')


def login(request):
    print(request)
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        print(account, password)
        if Member.objects.filter(account=account).exists():
            user = Member.objects.get(account=account)
            if user.password != password:
                return HttpResponse('wrong')
            else:
                return HttpResponse('right')
        else:
            return HttpResponse('not exist')


