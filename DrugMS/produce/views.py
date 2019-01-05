from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142
from user.models import supply5142,staff5142
from stock.models import shop5142,bill5142,stock5142
from django.db import transaction


from django.contrib.auth.decorators import login_required
def produce_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str = queryset2list(ill_slugs)

    supply_slugs = supply5142.objects.values_list('sname')
    supply_slug_str=queryset2list(supply_slugs)

    shop_slugs = shop5142.objects.values_list('pname')
    shop_slug_str = queryset2list(shop_slugs)


    ill_slug = request.GET.get('ill','')
    supply_slug = request.GET.get('supply','')
    shop_slug = request.GET.get('shop','')
    drug_done = choose(request,ill_slug,shop_slug,supply_slug,1)
    drug_doing = choose(request,ill_slug,shop_slug,supply_slug,0)
    return render(request,
                  'produce_index.html',
                  {
                    'supply_category':supply_slug,
                    'supply_categorys':supply_slug_str,
                    'shop_category':shop_slug,
                    'shop_categorys':shop_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': drug_done,
                      'products2':drug_doing
                  })

def choose(request,ill_slug,shop_slug,supply_slug,key):
    supply = request.user
    supply_object = supply5142.objects.get(sno=supply)
    drug_done = bill5142.objects.filter(s_done=key,sno=supply_object)
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        drug_done = drug_done.filter(dno__in=ill_dnos)
    if shop_slug !='':
        shop_dno = shop5142.objects.filter(pname=shop_slug)
        admin_ano = staff5142.objects.filter(ano__in=shop_dno)
        drug_done = drug_done.filter(ano__in=admin_ano)
    if supply_slug != '':
        supply_sno = supply5142.objects.filter(sname=supply_slug)
        drug_done = drug_done.filter(sno__in=supply_sno)
    shop_pnos=queryset2list(drug_done.values_list('ano'))
    result_2=[]
    for i in range(0,len(drug_done)):
        result_1=[]
        result_1.append(drug_done[i])
        result_1.append(shop5142.objects.get(pno=shop_pnos[i]))
        result_2.append(result_1)
    return result_2

def queryset2list(a):
    shop_slug_str=[]
    for i in a:
        shop_slug_str.append(''.join(i))
    return shop_slug_str

@login_required
def make_drug(request):
    if request.method == 'POST':
        try:
            supply=request.user
            supply_object=supply5142.objects.get(sno=supply)
        except:
            return redirect('/index/', )

        # try:
        if True:
            bno = request.POST.get('bno_')
            per_b_money = request.POST.get('per_b_money_')
            with transaction.atomic():
                bill=bill5142.objects.get(bno=bno)
                bill.s_done=1
                money1=bill.per_b_money
                ano=bill.ano.ano
                shop_object=shop5142.objects.get(pno=ano)
                bill.per_b_money=per_b_money
                bill.save()
                stock5142.objects.create(pno=shop_object,dno=bill.dno,d_count=bill.drug_b_count,per_p_money=money1)
            return redirect('/supply/',)
        # except:
        #     return redirect('/index/', )
