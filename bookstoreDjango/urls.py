"""bookstoreDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views as api_views


urlpatterns = [
    path('', api_views.setIndex),
    path('admin/', admin.site.urls),
    path('bookstore/', include('bookstore.urls')),
    path('getTeam/', api_views.getTeam),
    path('GETTest/', api_views.GETTest),
    path('POSTTest/', api_views.POSTTest),
    path('login/', api_views.login),
    path('verify/', api_views.verify),
    path('register/', api_views.register),
    path('poster/', api_views.poster),
    path('bookList/', api_views.bookList),
    path('bookInfo/', api_views.bookInfo),
    path('shoppingList/', api_views.shoppingList),
    path('addToCart/', api_views.addToCart),
    path('submitOrder/', api_views.submitOrder),
    path('deleteFromCart/', api_views.deleteFromCart),
    path('orderList/', api_views.orderList),
    path('downloadBook/', api_views.downloadBook),



]
