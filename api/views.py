from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

from django.db.models import Q

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

from django.core.mail import send_mail
from bookstoreDjango import settings
import random
def verify(request):
    if request.method == 'POST':
        print(request)
        targetEmail = request.POST.get('email')
        sub = '欢迎使用网上书店！'
        code = ''
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            code += ch
        msg = '您的验证码为：' + code

        if EmailVerify.objects.filter(email=targetEmail).exists():
            return HttpResponse('email exist')
        else:
            send_mail(
                subject=sub,
                message=msg,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    targetEmail,
                ]
            )
            if EmailVerify.objects.filter(email=targetEmail).exists():
                EmailVerify.objects.get(email=targetEmail).update(verifyCode=code)
            else:
                EmailVerify.objects.create(email=targetEmail, verifyCode=code)
            return HttpResponse('success')


def register(request):
    if request.method == 'POST':
        acc = request.POST.get('account')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        verifyCode = request.POST.get('verifyCode')

        if User.objects.filter(account=acc).exists():
            return HttpResponse('account exist')
        elif User.objects.filter(email=email).exists():
            return HttpResponse('email exist')
        else:
            print(email)
            print(EmailVerify.objects.get(email=email).verifyCode)
            if EmailVerify.objects.get(email=email).verifyCode != verifyCode:
                return HttpResponse('verifyCode wrong')
            else:
                User.objects.create(
                    account=acc,
                    password=pwd,
                    email=email,
                    name=name,
                )

                return HttpResponse('success')

