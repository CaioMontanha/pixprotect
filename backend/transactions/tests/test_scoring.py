from datetime import datetime, timedelta, timezone
from decimal import Decimal
from django.test import SimpleTestCase
from transactions.scoring import score_transaction

class ScoringTests(SimpleTestCase):
    def tx(self, **changes):
        value = {"valor": Decimal("100.00"), "occurred_at": datetime(2025, 1, 15, 12, 0, tzinfo=timezone.utc), "conta": "a", "chave_destino": "key", "uf_origem": "SP", "uf_destino": "SP"}
        return {**value, **changes}

    def score(self, tx=None, history=None):
        return score_transaction(tx or self.tx(), history or [ ("key", datetime(2025, 1, 1, tzinfo=timezone.utc)) ])

    def test_amount_over_2000(self):
        self.assertEqual(self.score(self.tx(valor=Decimal("2000.01")))[0], 15)

    def test_amount_over_5000(self):
        self.assertEqual(self.score(self.tx(valor=Decimal("5000.01")))[0], 30)

    def test_amount_boundaries(self):
        self.assertEqual(self.score(self.tx(valor=Decimal("2000.00")))[0], 0)
        self.assertEqual(self.score(self.tx(valor=Decimal("2000.01")))[0], 15)
        self.assertEqual(self.score(self.tx(valor=Decimal("5000.00")))[0], 15)
        self.assertEqual(self.score(self.tx(valor=Decimal("5000.01")))[0], 30)

    def test_night_boundary(self):
        base = self.tx()
        at_459 = base["occurred_at"].replace(hour=4, minute=59)
        at_500 = base["occurred_at"].replace(hour=5, minute=0)
        self.assertEqual(self.score(self.tx(occurred_at=at_459))[0], 20)
        self.assertEqual(self.score(self.tx(occurred_at=at_500))[0], 0)

    def test_new_recipient(self):
        self.assertEqual(self.score(self.tx(chave_destino="new"))[0], 25)

    def test_different_states(self):
        self.assertEqual(self.score(self.tx(uf_destino="RJ"))[0], 10)

    def test_burst_needs_four_and_inclusive_window(self):
        current = self.tx()["occurred_at"]
        three = [("key", current - timedelta(minutes=i)) for i in (1, 2, 3)]
        four = three + [("x", current - timedelta(minutes=10))]
        self.assertEqual(self.score(self.tx(), three)[0], 0)
        self.assertEqual(self.score(self.tx(), four)[0], 15)
        outside = [("key", current - timedelta(minutes=10, seconds=1))] * 4
        self.assertEqual(self.score(self.tx(), outside)[0], 0)

    def test_maximum_is_100(self):
        current = self.tx()["occurred_at"].replace(hour=3)
        history = [("other", current - timedelta(minutes=i)) for i in range(1, 5)]
        tx = self.tx(valor=Decimal("5000.01"), occurred_at=current, chave_destino="new", uf_destino="RJ")
        self.assertEqual(self.score(tx, history)[0], 100)

    def test_documented_transaction_83921(self):
        current = self.tx()["occurred_at"].replace(hour=3, minute=17)
        tx = self.tx(valor=Decimal("4850.00"), occurred_at=current, chave_destino="83921-dest", uf_origem="PE", uf_destino="SP")
        score, level, reasons = self.score(tx, [])
        self.assertEqual((score, level, len(reasons)), (70, "alto", 4))
