# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('formated_account_id', 'balance', 'currency', 'created')

    def formated_account_id(self, obj):
        return "{:08d}".format(obj.id)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'get_currency', 'source', 'destination', 'name', 'created')
    exclude = ('name',)

    def get_currency(self, obj):
        if obj.name == 'TRANSFER':
            return obj.source.currency
        elif obj.name == 'DEPOSIT':
            return obj.destination.currency
        else:
            return obj.source.currency

    get_currency.short_description = "CURRENCY"
