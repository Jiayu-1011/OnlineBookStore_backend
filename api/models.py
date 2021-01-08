from django.db import models

# Create your models here.

# 数据库中的表

# User(account, password, name, identity, email, balance)
class User(models.Model):
    account = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    identity = models.CharField(max_length=64, default='member') #用户身份 有visitor（游客）、member（会员）、admin（管理员）
    email = models.CharField(max_length=64) #用户邮箱
    balance = models.FloatField(default=0) #余额


# Book(bookId, name, price, writer, bookClass, salesPerMonth, publishTime, publisher,
#      commentLevel, iventory, briefIntro, imgUrl)
class Book(models.Model):

    bookId = models.CharField(max_length=64, primary_key=True) #书名+出版时间，如 三体20201230
    name = models.CharField(max_length=64) #书名
    price = models.FloatField(max_length=64) #价格
    writer = models.CharField(max_length=64, default='') #作者
    bookClass = models.CharField(max_length=64, default='') #类别 children/science/english/textbook
    salesPerMonth = models.IntegerField(default=0) #月销量
    publishTime = models.DateField(default='2019-01-01') #出版时间
    publisher = models.CharField(max_length=50, default='unknown') #出版社
    commentLevel = models.IntegerField(default=0) #评价等级 从0-5表示星数
    inventory = models.IntegerField(default=0) #库存量
    briefIntro = models.CharField(max_length=100, default='') #简介
    imgUrl = models.CharField(max_length=100, default='') # 书籍封面图片url,服务器上绝对路径,放在/sources/bookstore/cover/下面
    eBookUrl = models.CharField(max_length=100, default='') # 电子书文件url


class EmailVerify(models.Model):
    email = models.CharField(max_length=64, primary_key=True) #用户邮箱
    verifyCode = models.CharField(max_length=20)  #邮箱验证码

class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=64)
    bookId = models.CharField(max_length=64)

class Order(models.Model):
    orderId = models.CharField(max_length=64, primary_key=True) #订单编号
    account = models.CharField(max_length=64)
    goods = models.CharField(max_length=1000) #图书编号列表
    orderTime = models.DateTimeField() #下单时间
    orderPrice = models.FloatField() #订单金额




