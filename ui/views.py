# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from api.models import Account, Transaction


def index(request):
    return HttpResponse("Test s4u")


class AccountView(TemplateView):
    template_name = 'accounts.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        accounts = Account.objects.all()

        paginator = Paginator(accounts, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['accounts'] = show_lines
        return context


class TransactionView(TemplateView):
    template_name = 'transactions.html'

    def get_context_data(self, **kwargs):
        context = super(TransactionView, self).get_context_data(**kwargs)
        transactions = Transaction.objects.all()

        paginator = Paginator(transactions, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['transactions'] = show_lines
        return context
