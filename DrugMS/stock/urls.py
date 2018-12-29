from django.conf.urls import url
from .views import stock_list

urlpatterns = [
    url(r'^', stock_list),
]
