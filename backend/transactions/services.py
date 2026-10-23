from django.db import transaction
from django.db.models import Max
from .models import Transaction
from .scoring import score_transaction

@transaction.atomic
def create_transaction(data):
    account = data["conta_origem"]
    history = list(Transaction.objects.filter(conta_origem=account, occurred_at__lt=data["occurred_at"]).values_list("chave_destino", "occurred_at"))
    score, level, reasons = score_transaction({"valor": data["valor"], "occurred_at": data["occurred_at"], "conta": account, "chave_destino": data["chave_destino"], "uf_origem": data["uf_origem"], "uf_destino": data["uf_destino"]}, history)
    if not data.get("codigo"):
        data["codigo"] = (Transaction.objects.aggregate(value=Max("codigo"))["value"] or 0) + 1
    return Transaction.objects.create(**data, risk_score=score, risk_level=level, reasons=reasons)
