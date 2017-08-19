# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from fixerio import Fixerio


class Account(models.Model):
    """
    class description
    """
    CURRENCY_CHOICES = (
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('GBP', 'GBP'),
            ('CHF', 'CHF'),
    )

    id = models.AutoField(
        primary_key=True
    )

    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='USD')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        self.balance -= amount
        self.save()

    def __str__(self):
        return "{:08d}".format(self.id)

    def get_absolute_url(self):
        return "/api/accounts/%i/" % self.id


class Transaction(models.Model):
    """
    Transaction
    """

    name = models.CharField(verbose_name='OPERATION', max_length=10, blank=True, null=True)
    source = models.ForeignKey('Account', related_name='source', blank=True, null=True)
    destination = models.ForeignKey('Account', related_name='destination', blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def currencty_converer(self, amount, src, dst):
        fxrio = Fixerio(base=src.currency)
        result = fxrio.latest()
        rate = result['rates'].get(dst.currency)

        if rate:
            print rate
            import decimal
            amount *= decimal.Decimal(rate)
        return amount

    def save(self, *args, **kwargs):
        if not self.source:
            self.destination.deposit(self.amount)
            self.name = 'DEPOSIT'
        elif not self.destination:
            self.source.withdraw(self.amount)
            self.name = 'WITHDRAWAL'
        else:
            self.name = 'TRANSFER'
            self.source.withdraw(self.amount)
            amount = self.currencty_converer(self.amount, self.source, self.destination)
            self.destination.deposit(amount)
        super(Transaction, self).save(*args, **kwargs)
