from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142,produce5142
from user.models import supply5142

def produce_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str=[]
    for i in ill_slugs:
        ill_slugs_str.append(''.join(i))

    supply_slugs = supply5142.objects.values_list('sname')
    supply_slug_str=[]
    for i in supply_slugs:
        supply_slug_str.append(''.join(i))

    products = drug5142.objects.filter()
    ill_slug = request.GET.get('ill','')
    supply_slug = request.GET.get('supply','')
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        products = products.filter(dno__in=ill_dnos)
    if supply_slug !='':
        drug_snos = supply5142.objects.filter(sname=supply_slug)
        products = products.filter(sno__in=drug_snos)
    return render(request,
                  'produce_index.html',
                  {
                    'supply_category':supply_slug,
                    'supply_categorys':supply_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': products
                  })
