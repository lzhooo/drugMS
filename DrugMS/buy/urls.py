from django.conf.urls import url
from .views import durg_list,buy_drug

urlpatterns = [
    url(r'^buy/', buy_drug),
    url(r'^', durg_list),
]
