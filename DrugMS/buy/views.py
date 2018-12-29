from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142
from stock.models import stock5142
from stock.models import shop5142
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
