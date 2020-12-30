from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

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
        if User.objects.filter(account=account).exists():
            user = User.objects.get(account=account)
            if user.password != password:
                return JsonResponse({
                    'msg': 'wrong',
                })
            else:
                return JsonResponse({
                    'msg': 'right',
                    'identity': user.identity,
                    'name': user.name,
                })
        else:
            return JsonResponse({
                    'msg': 'not exist',
                })


def poster(request):
    print(request)
    if request.method == 'GET':
        poster_path = '/sources/bookstore/poster'
        posterArr = []
        for root,dirs,files in os.walk(poster_path):
            for name in files:
                posterArr.append('http://119.29.24.77' + os.path.join(root, name))


        print(posterArr)
        return JsonResponse({
            'posterArr': posterArr,
        })


def bookList(request):
    if request.method == 'GET':
        print(request)
        if request.GET.get('name') != '':
            bookName = request.GET.get('name')
            book = Book.objects.filter(name=bookName)
        else:
            bookClass = request.GET.get('bookClass')
            book = Book.objects.filter(bookClass=bookClass)
        print(book)
        bookArr = []
        for item in book:
            bookArr.append({
                'bookId': item.bookId, # 书名 + 出版时间，如三体20201230
                'bookClass': item.bookClass,
                'imgUrl': item.imgUrl,
                'name': item.name,
                'price': item.price,
                'salesPerMonth': item.salesPerMonth, # 月销量
                'publishTime': item.publishTime,
                'publisher': item.publisher,
                'commentLevel': item.commentLevel,
                'inventory': item.inventory,
            })

        return JsonResponse({
            'bookList': bookArr
        })



