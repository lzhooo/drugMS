from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142,produce5142
from stock.models import stock5142
from stock.models import shop5142

def stock_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str=queryset2list(ill_slugs)

    shop_slugs = list(set(shop5142.objects.values_list('pname')))
    shop_slug_str=queryset2list(shop_slugs)

    products = stock5142.objects.filter()
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
    drug_s_money=[]
    for i in range(0,len(drug_dno)):
        m=produce5142.objects.filter(dno=drug_dno[i],sno=drug_sno[i]).values("per_s_money").first()
        drug_s_money.append(m['per_s_money'])
    print(drug_s_money)
    print(products[0])
    result_2=[]
    for i in range(0,len(drug_dno)):
        result_1=[]
        result_1.append(products[i])
        result_1.append(drug_s_money[i])
        result_2.append(result_1)
        print(result_2)
    return render(request,
                  'stock_index.html',
                  {
                    'shop_category':shop_slug,
                    'shop_categorys':shop_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': result_2,
                  })

def queryset2list(a):
    shop_slug_str=[]
    for i in a:
        shop_slug_str.append(''.join(i))
    return shop_slug_str
