from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ExpertSearch.as_view(), name='search'),
]
