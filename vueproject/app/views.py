from base64 import encode
from cmath import log
from re import T
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app.models import User, Gpxx, gp_list
import json
import requests
import datetime, time


def index(request):
    #return HttpResponse("111111111111111111")

    return render(request, 'index.html')
def ckmx(request):
    start = datetime.date(2022,5,13)
    end = datetime.date(2022,5,19)
    # result = gp_list.objects.filter(sj__year = '2022')
    result = gp_list.objects.filter(sj__range=(start,end))

    arr = []
    for i in result:
        content = {'name': i.name, 'dm': i.dm, 'sj': i.sj.__format__('%Y-%m-%d'), 'sp': i.sp}
        arr.append(content)
        print(arr)   
    return HttpResponse(arr)

def addUser(request):
    user = User()
    user.UserName = '向原平11111111'
    user.Address = '四川省成都市成华区二仙桥19路华林东苑4栋2单元1202'
    user.save()
    context = {}
    context['value'] = user.Address + '数据添加成功！'
    return render(request,'index.html',context)

def gplist(request):
    # for i in range(0, 5000):
    #         #如果id不为空，获取该字段，并将其删除，我们只删除book表，publisher表不变
    #         try:
    #             book_obj =Gpxx.objects.get(id=i)
    #             book_obj.delete()
    #         except:
    #             pass
    
    querysetlist=[]
    url = "http://89.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=4962&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048"
    data = requests.get(url).json()
    result = data['data']['diff']
    print(data['data']['diff'])
    for i in data['data']['diff']:
        print(i)
        querysetlist.append(
                Gpxx ( 
                    f1 = i['f1'],
                    f2 = i['f2'],
                    f3 = i['f3'],
                    f4 = i['f4'],
                    f5 = i['f5'],
                    f6 = i['f6'],
                    f7 = i['f7'],
                    f8 = i['f8'],
                    f9 = i['f9'],
                    f10 = i['f10'],
                    f11 = i['f11'],
                    f12 = i['f12'],
                    f13 = i['f13'],
                    f14 = i['f14'],
                    f15 = i['f15'],
                    f16 = i['f16'],
                    f17 = i['f17'],
                    f18 = i['f18'],
                    f19 = i['f19'],
                    f20 = i['f20'],
                    f21 = i['f21'],
                    f22 = i['f22'],
                    f23 = i['f23'],
                    f24 = i['f24'],
                    f25 = i['f25'],
                    f26 = i['f26'],
                    f27 = i['f27'],
                    f28 = i['f28'],
                    f29 = i['f29']
                )
        )
    Gpxx.objects.bulk_create(querysetlist)
    return HttpResponse(result)

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


    result = User.objects.filter(Address='四川省成都市成华区二仙桥19路华林东苑4栋2单元1202')
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

def lookGp(_self_):
    result = Gpxx.objects.all()
    arr = []
    for i in result:
        print()
        request(i.f13, i.f12)
        arr.append(i.f12)
    return HttpResponse(1111)

def request(lx, dm):
    url = "http://push2his.eastmoney.com/api/qt/stock/kline/get?fields1=f1,f2,f3%,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61&ut=7eea3edcaed734bea9cbfc24409ed989&klt=101&fqt=1&secid=type.name&beg=0&end=20500000&_=1651275671129"
    name = ''
    type = ''
    gpmc = ''
    gpdm = ''
    gpArr = []
    if lx:
        url = url.replace("name",dm)
        url = url.replace("type",lx)
        data = requests.get(url).json();
        print(data)
        gpmc =  data['data']['name'];
        gpdm =  data['data']['code'];
        for i in data['data']['klines']:
            print(i)
            sj = i.split(',')
            gpArr.append(
                    gp_list ( 
                        name = gpmc,
                        dm = gpdm,
                        sj = sj[0],
                        kp = sj[1],
                        sp = sj[2],
                        zg = sj[3],
                        zd = sj[4],
                        cjl = sj[5],
                        cle = sj[6],
                        zf = sj[7],
                        zdf = sj[8],
                        hs = sj[9]
                    )
            )
        gp_list.objects.bulk_create(gpArr)
        return HttpResponse(data)

    # else:
    # name = request.GET.get("name");
    # type = request.GET.get("type");
    # url = url.replace("name",name)
    # url = url.replace("type",type)
    # data = requests.get(url);
    # print(url);
    # print(name,type);
    # return HttpResponse(data)

def alllist(request):
    url = "http://89.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=4962&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048"
    data = requests.get(url) 
    print(data)

    return HttpResponse(data)

def test():
    #   d =  datetime.date(2022, 4, 8)
    #   d.__format__('%Y-%M-%D')
    #   print(d)


    # result = gp_list.objects.filter(sj__year = '2022')
    # arr = []
    # for i in result:
    #     content = {'name': i.name, 'dm': i.dm, 'sj': i.sj.__format__('%Y-%m-%d'), 'sp': i.sp}
    #     arr.append(content)
    #     print(arr)

    print(time.strptime('2022-12-12', "%Y-%m-%d") > time.strptime('2022-12-13', "%Y-%m-%d"))

test()