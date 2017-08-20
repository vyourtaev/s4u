from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.http import HttpResponse
from ui.views import AccountView, AccountDetailView, TransactionView
from ui.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^accounts$', AccountView.as_view(), name='accounts'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', AccountDetailView.as_view()),
    url(r'^transactions$', TransactionView.as_view(), name='transactions'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
