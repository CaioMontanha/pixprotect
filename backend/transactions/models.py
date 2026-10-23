from django.db import models

class Transaction(models.Model):
    class RiskLevel(models.TextChoices):
        LOW = "baixo", "Baixo"
        MEDIUM = "medio", "Médio"
        HIGH = "alto", "Alto"

    codigo = models.PositiveIntegerField(unique=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    occurred_at = models.DateTimeField()
    conta_origem = models.CharField(max_length=120, db_index=True)
    cidade_origem = models.CharField(max_length=100)
    uf_origem = models.CharField(max_length=2)
    chave_destino = models.CharField(max_length=160)
    nome_destino = models.CharField(max_length=160)
    cidade_destino = models.CharField(max_length=100)
    uf_destino = models.CharField(max_length=2)
    risk_score = models.PositiveSmallIntegerField()
    risk_level = models.CharField(max_length=8, choices=RiskLevel.choices)
    reasons = models.JSONField(default=list)
    is_demo = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-occurred_at", "-id"]
        indexes = [models.Index(fields=["conta_origem", "occurred_at"], name="tx_account_time_idx"), models.Index(fields=["risk_score"], name="tx_risk_score_idx")]

    def __str__(self):
        return f"PIX #{self.codigo}"
