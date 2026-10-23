import random
from datetime import timedelta
from decimal import Decimal
from django.db.models import Avg, Count, Sum
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .filters import TransactionFilter
from .models import Transaction
from .serializers import TransactionSerializer
from .services import create_transaction

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter
    ordering_fields = ["occurred_at", "risk_score", "valor", "codigo"]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = create_transaction(serializer.validated_data)
        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)

class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view(["GET"])
def dashboard_summary(request):
    qs = Transaction.objects.all()
    counts = {level: qs.filter(risk_level=level).count() for level, _ in Transaction.RiskLevel.choices}
    total = qs.count()
    high_value = qs.filter(risk_level="alto").aggregate(value=Sum("valor"))["value"] or Decimal("0.00")
    average = qs.aggregate(score=Avg("risk_score"))["score"] or 0
    by_hour = {row["hour"]: row for row in qs.values(hour=__import__("django.db.models.functions", fromlist=["ExtractHour"]).ExtractHour("occurred_at")).annotate(quantidade=Count("id"), score_medio=Avg("risk_score"))}
    return Response({"total": total, "por_nivel": counts, "valor_total_alto_risco": str(high_value), "score_medio": round(average), "dados_demonstracao": qs.filter(is_demo=True).exists(), "por_hora": [{"hora": h, "quantidade": by_hour[h]["quantidade"], "score_medio": round(by_hour[h]["score_medio"])} if h in by_hour else {"hora": h, "quantidade": 0, "score_medio": 0} for h in range(24)]})

@api_view(["POST"])
def simulate_transaction(request):
    now = timezone.now()
    examples = [("conta-demo-01", "São Paulo", "SP", "Curitiba", "PR"), ("conta-demo-02", "Recife", "PE", "Recife", "PE"), ("conta-demo-03", "Belo Horizonte", "MG", "Rio de Janeiro", "RJ")]
    account, city_from, uf_from, city_to, uf_to = random.choice(examples)
    data = {"valor": Decimal(str(random.choice([85, 240, 690, 2300, 6200]))), "occurred_at": now, "conta_origem": account, "cidade_origem": city_from, "uf_origem": uf_from, "chave_destino": f"demo-{random.randrange(100000, 999999)}@pixprotect.local", "nome_destino": "Destinatário de demonstração", "cidade_destino": city_to, "uf_destino": uf_to, "is_demo": True}
    transaction = create_transaction(data)
    return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
