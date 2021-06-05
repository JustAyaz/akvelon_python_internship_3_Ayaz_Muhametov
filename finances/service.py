from django_filters import rest_framework as filters
from finances.models import Transaction


# here i really wanted to understand how to filter by date with django_filter, but never used it
# because DailyTotal was broken
class TransactionFilter(filters.FilterSet):
    date = filters.RangeFilter()

    class Meta:
        model = Transaction
        fields = ['date']