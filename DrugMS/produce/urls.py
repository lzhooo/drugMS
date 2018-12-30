from django.conf.urls import url
from .views import produce_list,make_drug

urlpatterns = [
    url(r'^make/', make_drug),
    url(r'^', produce_list),

]
