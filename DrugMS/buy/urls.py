from django.conf.urls import url
from .views import durg_list

urlpatterns = [
    url(r'^c_index/(?P<ill_slug>[-\w]+)', durg_list),
    url(r'^c_index/', durg_list),
]
