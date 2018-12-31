from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142
from stock.models import stock5142
from stock.models import shop5142
from user.models import customer5142
from buy.models import buy5142
from django.db import transaction
# Create your views here.
def customerindex(request):
    return render(request,'customer_index.html')

def durg_list(request):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str=[]
    for i in ill_slugs:
        ill_slugs_str.append(''.join(i))

    shop_slugs = list(set(shop5142.objects.values_list('pname')))
    shop_slug_str=[]
    for i in shop_slugs:
        shop_slug_str.append(''.join(i))

    products = stock5142.objects.filter()
    ill_slug = request.GET.get('ill','')
    shop_slug = request.GET.get('shop','')
    if ill_slug != '':
        ill_dnos = drug5142.objects.filter(dill=ill_slug)
        products = products.filter(dno__in=ill_dnos)
    if shop_slug !='':
        shop_dno = shop5142.objects.filter(pname=shop_slug)
        products = products.filter(pno__in=shop_dno)
    return render(request,
                  'customer_index.html',
                  { 'shop_category':shop_slug,
                    'shop_categorys':shop_slug_str,
                    'category': ill_slug,
                    'categories':ill_slugs_str,
                    'products': products})

# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product})
from django.contrib.auth.decorators import login_required
@login_required
def buy_drug(request):
    try:
        customer=request.user
        customer_object=customer5142.objects.get(cno=customer)
    except:
        return redirect('/index/', )
    pname=request.POST.get('pname_')
    dno=request.POST.get('dno_')
    d_count=int(request.POST.get('d_count_'))
    drug_object = drug5142.objects.filter(dno=dno).first()
    shop_object = shop5142.objects.filter(pname=pname).first()
    print(customer_object,drug_object,shop_object)
    with transaction.atomic():
        try:
            money=stock5142.objects.filter(pno=shop_object,dno=drug_object).values_list('per_p_money').first()[0]
            count=stock5142.objects.filter(pno=shop_object,dno=drug_object).values_list('d_count').first()[0]
        except:
            return redirect('/index/', )
        if count < d_count:
            return redirect('/index/', )
        new_count = count - d_count
        stock5142.objects.filter(pno=shop_object,dno=drug_object).update(d_count=new_count)
        buy5142.objects.create(dno=drug_object,cno=customer_object,pno=shop_object,per_c_money=money,drug_b_count=d_count)
    return redirect('/customer/', )
