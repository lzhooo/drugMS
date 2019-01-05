from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142
from stock.models import stock5142,bill5142
from stock.models import shop5142
from user.models import supply5142,staff5142

from django.contrib.auth.decorators import login_required

def stock_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str=queryset2list(ill_slugs)

    shop_slugs = list(set(shop5142.objects.values_list('pname')))
    shop_slug_str=queryset2list(shop_slugs)
    ano=request.user
    admin_object = staff5142.objects.get(ano=ano)
    shop_object = shop5142.objects.get(pno=admin_object.ano)
    products = stock5142.objects.filter(pno=shop_object)
    ill_slug = request.GET.get('ill','')
    shop_slug = request.GET.get('shop','')
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        products = products.filter(dno__in=ill_dnos)
    if shop_slug !='':
        shop_dno = shop5142.objects.filter(pname=shop_slug)
        products = products.filter(pno__in=shop_dno)

    drug_dno = products.values_list("dno")
    drug_dno = queryset2list(drug_dno)

    drug_sno=[]
    for i in drug_dno:
        d=drug5142.objects.filter(dno=i).values("sno").first()
        drug_sno.append(d['sno'])
    #这里筛选
    drug_b_money=[]
    for i in range(0,len(drug_dno)):
        m=bill5142.objects.filter(dno=drug_dno[i],sno=drug_sno[i]).values("per_b_money").first()
        drug_b_money.append(m['per_b_money'])
    #end
    result_2=[]
    if len(drug_dno)>0:
        for i in range(0,len(drug_dno)):
            result_1=[]
            result_1.append(products[i])
            result_1.append(drug_b_money[i])
            result_2.append(result_1)
            print(result_2)

    drug_doing = bill5142.objects.filter(s_done=0,ano=admin_object)
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        drug_doing = drug_doing.filter(dno__in=ill_dnos)
    if shop_slug !='':
        shop_dno = shop5142.objects.filter(pname=shop_slug)
        admin_ano = staff5142.objects.filter(ano__in=shop_dno)
        drug_doing = drug_doing.filter(ano__in=admin_ano)

    return render(request,
                  'stock_index.html',
                  {
                    'shop_category':shop_slug,
                    'shop_categorys':shop_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': result_2,
                      'drug_doing':drug_doing
                  })

def queryset2list(a):
    shop_slug_str=[]
    for i in a:
        shop_slug_str.append(''.join(i))
    return shop_slug_str

import time
@login_required
def stock_drug(request):
    try:
        shop=request.user
        staff_object=staff5142.objects.get(ano=shop,aposition='admin')
    except:
        return redirect('/index/', )
    dno = request.POST.get('dno_')
    sname = request.POST.get('sname_')
    dill = request.POST.get('dill_')
    dname = request.POST.get('dname_')
    drug_b_count = request.POST.get('drug_b_count_')
    per_b_money = request.POST.get('per_b_money_')
    supply_object = supply5142.objects.get(sname=sname)
    drug_object=drug5142.objects.filter(dno=dno).first()
    time.sleep(0.2)
    ts=str(int(round(time.time()*1000)))
    if not drug_object:
        drug_object=drug5142.objects.create(dno=dno,sno=supply_object,dname=dname,dill=dill)
    bill5142.objects.create(bno=ts,ano=staff_object,dno=drug_object,sno=supply_object,drug_b_count=drug_b_count,per_b_money=per_b_money)
    return redirect('/shop/', )



