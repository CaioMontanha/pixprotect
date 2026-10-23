import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    min_score = django_filters.NumberFilter(field_name="risk_score", lookup_expr="gte")
    conta = django_filters.CharFilter(field_name="conta_origem", lookup_expr="icontains")
    class Meta:
        model = Transaction
        fields = ["risk_level"]
