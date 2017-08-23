# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.detail import DetailView
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

        paginator = Paginator(accounts, 5)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['accounts'] = show_lines
        return context


class AccountDetailView(DetailView):
    template_name = "account_details.html"
    context_object_name = "account"
    model = Account

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        transactions = self.get_object().source.all()
        paginator = Paginator(transactions, 5)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['transactions'] = show_lines
        return context


class TransactionView(TemplateView):
    template_name = 'transactions.html'

    def get_context_data(self, **kwargs):
        context = super(TransactionView, self).get_context_data(**kwargs)
        transactions = Transaction.objects.all()

        paginator = Paginator(transactions, 5)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context['transactions'] = show_lines
        return context
