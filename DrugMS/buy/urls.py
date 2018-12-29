from django.conf.urls import url
from .views import durg_list

urlpatterns = [
    url(r'^', durg_list),
]
