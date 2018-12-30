from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142,produce5142
from user.models import supply5142,staff5142
from stock.models import shop5142,bill5142

def produce_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str = queryset2list(ill_slugs)

    supply_slugs = supply5142.objects.values_list('sname')
    supply_slug_str=queryset2list(supply_slugs)

    shop_slugs = shop5142.objects.values_list('pname')
    shop_slug_str = queryset2list(shop_slugs)

    products = produce5142.objects.filter()
    ill_slug = request.GET.get('ill','')
    supply_slug = request.GET.get('supply','')
    shop_slug = request.GET.get('shop','')
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        products = products.filter(dno__in=ill_dnos)
    if supply_slug !='':
        drug_snos = supply5142.objects.filter(sname=supply_slug)
        products = products.filter(sno__in=drug_snos)
    # if shop_slug !='':

    drug_dno = products.values_list("dno")
    drug_dno = queryset2list(drug_dno)
    drug_sno = products.values_list("sno")
    drug_sno = queryset2list(drug_sno)
    result_2=[]
    for i in range(0,len(drug_dno)):
        result_1=[]
        if shop_slug !='':
            shop_pnos = shop5142.objects.filter(pname=shop_slug).values("pno").first()
            print(shop_pnos)
            m = bill5142.objects.filter(dno=drug_dno[i], sno=drug_sno[i],ano=shop_pnos['pno']).values("ano", "drug_b_count").first()
        else:
            m=bill5142.objects.filter(dno=drug_dno[i],sno=drug_sno[i]).values("ano","drug_b_count").first()
        if m:
            result_1.append(products[i])
            n=shop5142.objects.filter(pno=m['ano']).values("pname").first()
            result_1.append(n['pname'])
            result_1.append(m['drug_b_count'])
            result_2.append(result_1)
    print(result_2)



    return render(request,
                  'produce_index.html',
                  {
                    'supply_category':supply_slug,
                    'supply_categorys':supply_slug_str,
                    'shop_category':shop_slug,
                    'shop_categorys':shop_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': result_2
                  })

def queryset2list(a):
    shop_slug_str=[]
    for i in a:
        shop_slug_str.append(''.join(i))
    return shop_slug_str