from django.conf.urls import url
from .views import login,regist,logout,index

urlpatterns = [
    url(r'^login/', login),
    url(r'^regist/', regist),
    url(r'^logout/', logout),
    url(r'^index/', index),
]