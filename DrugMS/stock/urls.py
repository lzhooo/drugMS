from django.conf.urls import url
from .views import stock_list,stock_drug

urlpatterns = [
    url(r'^stock/', stock_drug),
    url(r'^', stock_list),
]
