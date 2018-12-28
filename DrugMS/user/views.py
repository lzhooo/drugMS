from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import customer5142,staff5142,supply5142
from django.db import transaction

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密_码',widget=forms.PasswordInput())


def index(request):
    return render(request,'index.html')
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re = auth.authenticate(username=username,password=password)  #用户认证
        if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            auth.login(request,re)   #登陆成功
            return redirect('/user/index/',{'user':re})    #跳转--redirect指从一个旧的url转到一个新的url
        else:  #数据库里不存在与之对应的数据
            return render(request,'login.html',{'login_error':'用户名或密码错误'})  #注册失败
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  # 包含用户名和密码
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']  # cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']
            kind = request.POST.get('kind')
            # 添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            with transaction.atomic():
                registAdd = User.objects.create_user(username=username, password=password)
                if kind =="1":#顾客注册 顾客表5142增加数据
                    csex=request.POST.get('csex')
                    cname=request.POST.get('cname')
                    customer5142.objects.create(cno=username, csex=csex, cname=cname)
                if kind =="2":#供应商注册 供应商5142表增加数据
                    sname=request.POST.get('sname')
                    schat=request.POST.get('schat')
                    sadress=request.POST.get('sadress')
                    supply5142.objects.create(sno=username, sname=sname, schat=schat,sadress=sadress)

                if kind =="3":#员工注册 员工5142增加数据
                    aname=request.POST.get('aname')
                    aposition=request.POST.get('aposition')
                    staff5142.objects.create(ano=username, aname=aname, aposition=aposition)
                # print registAdd
            if registAdd == False:
                return render(request, 'regist.html', {'registAdd': registAdd, 'username': username})

            else:

                return render(request, 'login.html', {'registAdd': registAdd})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request, 'regist.html', {'uf': uf})

