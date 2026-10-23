from datetime import datetime, timezone
from django.test import TestCase
from rest_framework.test import APIClient
from transactions.models import Transaction

class TransactionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {"valor": "4850.00", "occurred_at": datetime(2025, 1, 15, 3, 17, tzinfo=timezone.utc).isoformat(), "conta_origem": "conta-teste", "cidade_origem": "Recife", "uf_origem": "PE", "chave_destino": "chave-teste", "nome_destino": "Teste", "cidade_destino": "São Paulo", "uf_destino": "SP", "risk_score": 0, "risk_level": "baixo", "reasons": []}

    def test_post_calculates_score_ignoring_client_score(self):
        response = self.client.post("/api/transactions", self.payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["risk_score"], 70)
        self.assertEqual(response.data["risk_level"], "alto")
        self.assertEqual(len(response.data["reasons"]), 4)
        self.assertEqual(Transaction.objects.get().risk_score, 70)

    def test_rejects_nonpositive_value(self):
        self.payload["valor"] = "0"
        self.assertEqual(self.client.post("/api/transactions", self.payload, format="json").status_code, 400)

    def test_summary_has_24_buckets(self):
        response = self.client.get("/api/dashboard/summary")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["por_hora"]), 24)
