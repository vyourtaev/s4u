from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.http import HttpResponse
from ui.views import AccountView, TransactionView
from ui.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^accounts$', AccountView.as_view(), name='accounts'),
    url(r'^transaction$', TransactionView.as_view(), name='transactions'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
