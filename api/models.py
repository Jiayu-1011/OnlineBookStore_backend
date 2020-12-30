from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    identity = models.CharField(max_length=64, default='member') #用户身份 有visitor（游客）、member（会员）、admin（管理员）



class Book(models.Model):

    bookId = models.CharField(max_length=64, primary_key=True) #书名+出版时间，如 三体20201230
    name = models.CharField(max_length=64) #书名
    price = models.FloatField(max_length=64) #价格
    bookClass = models.CharField(max_length=64, default='') #类别
    salesPerMonth = models.IntegerField(default=0) #月销量
    publishTime = models.DateField() #出版时间
    publisher = models.CharField(max_length=50, default='unknown') #出版社
    commentLevel = models.IntegerField(default=0) #评价等级 从0-5表示星数
    inventory = models.IntegerField(default=0) #库存量
    briefIntro = models.CharField(max_length=100, default='') #简介
    imgUrl = models.CharField(max_length=100, default='') #书籍封面图片url,服务器上绝对路径,放在/sources/bookstore/cover/下面





