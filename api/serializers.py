from rest_framework import serializers
from api.models import Account, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate_balance(self, balance, *args):
        if balance < 0:
            raise serializers.ValidationError("Negative balance is not allowed")
        return balance



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
