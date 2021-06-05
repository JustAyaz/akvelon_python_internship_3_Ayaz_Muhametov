from rest_framework import serializers
from finances.models import User, Transaction


# serializer for creating new users
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# serializer for creating new transaction
class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


# serializer for creating user's transactions list
class TransactionListSerializer(serializers.ModelSerializer):
    transactions = TransactionDetailSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


# serializer for creating total amount
class TransactionTotalSerializer(serializers.ModelSerializer):
    transactions = TransactionDetailSerializer(many=True)
    total_amount = serializers.IntegerField()

    class Meta:
        model = User
        fields = '__all__'


