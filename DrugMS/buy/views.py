from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from produce.models import drug5142
from stock.models import stock5142
# Create your views here.
def customerindex(request):
    return render(request,'customer_index.html')

def durg_list(request, ill_slug=None):
    ill_slugs =  list(set(drug5142.objects.values_list('dill')))
    ill_slugs_str=[]
    for i in ill_slugs:
        ill_slugs_str.append(''.join(i))
    products = drug5142.objects.filter()
    if ill_slug:
        print(ill_slug)
        products = products.filter(dill=ill_slug)
    return render(request,
                  'customer_index.html',
                  {'category': ill_slug,
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
