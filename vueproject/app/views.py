from base64 import encode
from cmath import log
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app.models import User
import json
import weibo
import requests
from bs4 import BeautifulSoup


def index(request):
    #return HttpResponse("111111111111111111")

    return render(request, 'index.html')

def addUser(request):
    user = User()
    user.UserName = '向原平'
    user.Address = '四川省成都市成华区二仙桥19路华林东苑4栋2单元1202'
    user.save()
    context = {}
    context['value'] = user.Address + '数据添加成功！'
    return render(request,'index.html',context)

def seeUser(request):
    # with open('../one.json','r') as load_f:
    #     data = json.load(load_f)
    #     APP_KEY = data['APP_KEY']
    #     APP_SECRET = data['APP_SECRET']
    #     print(APP_KEY, APP_SECRET)
    #     REDIRECT_URL = 'http://gulimall.com/success'

    #     client = weibo.Client(APP_KEY, APP_SECRET, REDIRECT_URL)
    #     authorize_url = client.authorize_url
    #     print(authorize_url)
    #     code= input('code>')
    #     client.set_code(code)
    #     user_data = client.get('users/show', uid=1282440983)
    #     print(user_data)


    result = User.objects.filter(UserName='向原平')
    arr = []
    for i in result:
        content = {'UserName': i.UserName, 'Address': i.Address}
        arr.append(content)
    return HttpResponse(arr)  

def userlist(request):
    name = request.GET.get("name")
    url = "https://searchapi.eastmoney.com/api/suggest/get?input=name&type=14&token=D43BF722C8E33BDC906FB84D85E326E8"
    url = url.replace("name",name)
    print(request.GET.get("name"))
    data = requests.get(url) 
    print(data)

    return HttpResponse(data)

def request(request):
    name = request.GET.get("name")
    type = request.GET.get("type")
    url = "http://push2his.eastmoney.com/api/qt/stock/kline/get?fields1=f1,f2,f3%,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61&ut=7eea3edcaed734bea9cbfc24409ed989&klt=101&fqt=1&secid=type.name&beg=0&end=20500000&_=1651275671129"
    url = url.replace("name",name)
    url = url.replace("type",type)
    print(name,type)
    data = requests.get(url) 
    print(data)

    return HttpResponse(data)
