from django.conf.urls import url
from .views import produce_list

urlpatterns = [
    url(r'^', produce_list),
]
