from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse,FileResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

from django.db.models import *

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


# 登录
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
                    'balance': user.balance,
                })
        else:
            return JsonResponse({
                    'msg': 'not exist',
                })


# 获取海报轮播图
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


from django.core.mail import send_mail
from bookstoreDjango import settings
import random

# （注册时）验证邮箱
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


# 注册账号
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


# 获取图书列表
def bookList(request):
    if request.method == 'GET':
        print(request)
        #搜索关键词
        if request.GET.get('name') != '':
            keyword = request.GET.get('name')
            allBook = Book.objects.all().values()
            book = []
            for item in allBook:
                regExp = r'.*' + keyword + r'.*'

                if re.search(regExp, item['name'], re.I) is not None:
                    name = re.search(regExp, item['name'], re.I).group()
                    simpleBook = Book.objects.filter(name=name).values()[0]
                    book.append(simpleBook)

        #选择类别
        elif request.GET.get('bookClass') != '':
            bookClass = request.GET.get('bookClass')
            book = Book.objects.filter(bookClass=bookClass).values()
        else:
            book = Book.objects.all().values()
        print(book)
        bookArr = []
        for item in book:
            print(item)

            bookArr.append(item)

        return JsonResponse({
            'bookList': bookArr
        })

# 获取图书详情
def bookInfo(request):
    if request.method == 'POST':
        print(request)
        targetBookIds = request.POST.get('bookId')
        targetIdArr = targetBookIds.split(';')
        info = []
        for targetBookId in targetIdArr:
            info_temp = Book.objects.filter(bookId=targetBookId).values()
            info.append(info_temp[0])


        return JsonResponse({
            'bookInfo': info,
        })


# 获取购物车列表
def shoppingList(request):
    if request.method == 'GET':
        print(request)
        account = request.GET.get('account')
        slist = ShoppingCart.objects.filter(account=account).values()
        data = []
        for item in slist:
            info = Book.objects.filter(bookId=item['bookId']).values()
            data.append(info[0])

        return JsonResponse({
            'shoppingList': data,

        })


# 商品添加至购物车
def addToCart(request):
    if request.method == 'POST':
        print(request)
        account = request.POST.get('account')
        bookId = request.POST.get('bookId')
        ShoppingCart.objects.create(account=account, bookId=bookId)
        return HttpResponse('success')


# 提交订单
import api.utils
def submitOrder(request):
    if request.method == 'POST':
        print(request)

        #生成订单添加到数据库
        generatedOrderId = api.utils.generateOrderId()
        # print(generatedOrderId())
        account = request.POST.get('account')
        orderTime = api.utils.generateFormatTime()
        print(orderTime)
        goods = request.POST.get('bookId')
        goodsArr = goods.split(',')
        orderPrice = 0
        for targetId in goodsArr:
            orderPrice += Book.objects.get(bookId=targetId).price

        Order.objects.create(
            orderId=generatedOrderId,
            goods=goods,
            account=account,
            orderTime=orderTime,
            orderPrice=orderPrice
        )

        #清空用户购物车中相应物品
        for targetId in goodsArr:
            ShoppingCart.objects.filter(bookId=targetId, account=account).delete()

        #扣除用户余额
        balance = User.objects.filter(account=account).values()[0]['balance'] - orderPrice
        User.objects.filter(account=account).update(balance=balance)

        return HttpResponse()


def deleteFromCart(request):
    if request.method == 'POST':
        print(request)
        account = request.POST.get('account')
        goods = request.POST.get('bookId')
        goodsArr = goods.split(',')
        # 清空用户购物车中相应物品
        for targetId in goodsArr:
            ShoppingCart.objects.filter(bookId=targetId, account=account).delete()

        return HttpResponse()


# 订单列表
def orderList(request):
    if request.method == 'GET':
        print(request)
        account = request.GET.get('account')
        oList = []
        for item in Order.objects.filter(account=account).values():
            oList.append(item)

        return JsonResponse({
            'orderList': oList,
        })



# 下载电子书
import re
def downloadBook(request):
    if request.method == 'GET':
        bookId = request.GET.get('bookId')
        eBookUrl = Book.objects.get(bookId=bookId).eBookUrl
        relativeUrl = re.search(r'\/sources.*', eBookUrl).group()
        fileName = eBookUrl.split('/')[-1]
        file = open(relativeUrl, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;file-name="1.pdf"'
        return response


#管理员添加图书
import base64
def addBook(request):
    if request.method == 'POST':
        print(request)
        bi = request.POST.dict()
        #生成bookId
        if 'publishTime' not in bi:
            bi['bookId'] = bi['name'] + '20190101'
        else:
            bi['bookId'] = api.utils.generateBookId(bi['name'], bi['publishTime'])

        #处理图书封面文件流
        if 'coverFile' in bi:
            coverFile = base64.b64decode(bi['coverFile'].split(',')[1])
            coverName = ''.join(bi['bookId'].split(':')) + '.jpg'
            coverPath = '/sources/bookstore/cover/' + coverName
            with open(coverPath, 'wb') as f:
                f.write(coverFile)
            del bi['coverFile']
            bi['imgUrl'] = 'http://119.29.24.77' + coverPath

        #处理电子书文件流
        if 'eBookFile' in bi:
            eBookFile = base64.b64decode(bi['eBookFile'].split(',')[1])
            eBookName = ''.join(bi['bookId'].split(':')) + '.pdf'
            eBookPath = '/sources/bookstore/eBook/' + eBookName
            with open(eBookPath, 'wb') as f:
                f.write(eBookFile)
            del bi['eBookFile']
            bi['eBookUrl'] = 'http://119.29.24.77' + eBookPath





        Book.objects.create(**bi)

        return HttpResponse()


# 修改图书信息
def modifyBook(request):
    if request.method == 'POST':
        print(request)
        bi = request.POST.dict()


        # #生成bookId
        # if 'publishTime' not in bi:
        #     bi['bookId'] = bi['name'] + '20190101'
        # else:
        #     bi['bookId'] = api.utils.generateBookId(bi['name'], bi['publishTime'])

        # #处理图书封面文件流
        # if 'coverFile' in bi:
        #     coverFile = base64.b64decode(bi['coverFile'].split(',')[1])
        #     coverName = ''.join(bi['bookId'].split(':')) + '.jpg'
        #     coverPath = '/sources/bookstore/cover/' + coverName
        #     with open(coverPath, 'wb') as f:
        #         f.write(coverFile)
        #     del bi['coverFile']
        #
        # #处理电子书文件流
        # if 'eBookFile' in bi:
        #     eBookFile = base64.b64decode(bi['eBookFile'].split(',')[1])
        #     eBookName = ''.join(bi['bookId'].split(':')) + '.pdf'
        #     eBookPath = '/sources/bookstore/eBook/' + eBookName
        #     with open(eBookPath, 'wb') as f:
        #         f.write(eBookFile)
        #     del bi['eBookFile']


        Book.objects.filter(bookId=bi['bookId']).update(**bi)

        return HttpResponse()


# 图书统计信息
def bookStats(request):
    if request.method == 'GET':
        print(request)
        classes = Book.objects.all().values('bookClass').distinct()
        classStats = []

        for item in classes:
            quantity = Book.objects.filter(bookClass=item['bookClass']).values().count()
            classStats.append({
                'class': item['bookClass'],
                'quantity': quantity,
            })


        return JsonResponse({
            'classStats': classStats
        })


# 获取用户列表
def userList(request):
    if request.method == 'GET':
        print(request)
        user = User.objects.all().values('name', 'account', 'balance')
        uList = []
        for item in user:
            uList.append(item)

        return JsonResponse({
            'userList': uList,
        })


# 充值
def recharge(request):
    if request.method == 'POST':
        print(request)
        ui = request.POST.dict()

        targetUser = User.objects.filter(account=ui['account']).values()[0]
        ui['balance'] = targetUser['balance'] + float(ui['balance'])
        User.objects.filter(account=ui['account']).update(balance=ui['balance'])

        return HttpResponse()


# 获取用户详情
def userInfo(request):
    if request.method == 'GET':
        print(request)
        account = request.GET.get('account')
        ui = User.objects.filter(account=account).values()[0]

        return JsonResponse({
            'userInfo': ui,
        })