import re
from datetime import timedelta
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    risk_score = serializers.IntegerField(read_only=True)
    risk_level = serializers.CharField(read_only=True)
    reasons = serializers.JSONField(read_only=True)
    anteriores_10_minutos = serializers.SerializerMethodField()
    is_demo = serializers.BooleanField(read_only=True)

    class Meta:
        model = Transaction
        fields = ["id", "codigo", "valor", "occurred_at", "conta_origem", "cidade_origem", "uf_origem", "chave_destino", "nome_destino", "cidade_destino", "uf_destino", "risk_score", "risk_level", "reasons", "anteriores_10_minutos", "is_demo", "created_at"]
        read_only_fields = ["id", "codigo", "created_at"]

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser maior que zero.")
        return value

    def validate_uf_origem(self, value):
        return self._validate_uf(value)

    def validate_uf_destino(self, value):
        return self._validate_uf(value)

    @staticmethod
    def _validate_uf(value):
        if not re.fullmatch(r"[A-Za-z]{2}", value):
            raise serializers.ValidationError("A UF deve conter exatamente duas letras.")
        return value.upper()

    def validate_chave_destino(self, value):
        if not value.strip():
            raise serializers.ValidationError("A chave de destino é obrigatória.")
        return value.strip()

    def get_anteriores_10_minutos(self, obj):
        start = obj.occurred_at - timedelta(minutes=10)
        qs = Transaction.objects.filter(conta_origem=obj.conta_origem, occurred_at__gte=start, occurred_at__lt=obj.occurred_at).order_by("occurred_at")
        return [{"codigo": row.codigo, "valor": str(row.valor), "occurred_at": row.occurred_at, "nome_destino": row.nome_destino} for row in qs]
