import random
from datetime import datetime, timedelta, time
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from transactions.models import Transaction
from transactions.services import create_transaction

class Command(BaseCommand):
    help = "Cria um conjunto reproduzível de transações PIX fictícias para desenvolvimento."

    @transaction.atomic
    def handle(self, *args, **options):
        random.seed(83921)
        Transaction.objects.all().delete()
        accounts = [f"conta-{i:02d}" for i in range(1, 16)]
        cities = [("São Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Belo Horizonte", "MG"), ("Curitiba", "PR"), ("Recife", "PE"), ("Porto Alegre", "RS"), ("Salvador", "BA")]
        now = timezone.now()
        start = now - timedelta(days=14)
        events = []
        for i in range(249):
            account = accounts[i % len(accounts)]
            city1, city2 = random.choice(cities), random.choice(cities)
            hour = random.choice([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) if random.random() > .08 else random.choice([1, 2, 3, 4])
            day = start + timedelta(seconds=random.randrange(0, int((now - start).total_seconds())))
            day = timezone.localtime(day)
            occurred = day.replace(hour=hour, minute=random.randrange(60), second=random.randrange(60), microsecond=0)
            value = Decimal(str(random.choice([45, 89.90, 120, 350, 780, 1500, 2400, 6100])))
            events.append((occurred, {"valor": value, "occurred_at": occurred, "conta_origem": account, "cidade_origem": city1[0], "uf_origem": city1[1], "chave_destino": f"chave-{account}-{random.randrange(12)}", "nome_destino": "Destinatário cadastrado", "cidade_destino": city2[0], "uf_destino": city2[1], "is_demo": True}))
        events.sort(key=lambda event: event[0])
        for _, data in events:
            create_transaction(data)
        # Registro documentado em docs.md: 4 razões, score 70.
        example_at = timezone.make_aware(datetime.combine(now.date(), time(3, 17, 42)))
        create_transaction({"codigo": 83921, "valor": Decimal("4850.00"), "occurred_at": example_at, "conta_origem": "conta-exemplo-83921", "cidade_origem": "Recife", "uf_origem": "PE", "chave_destino": "7a8b9c0d-1234-5678-9abc-def012345678", "nome_destino": "Roberto A. Duarte", "cidade_destino": "São Paulo", "uf_destino": "SP", "is_demo": True})
        self.stdout.write(self.style.SUCCESS(f"Seed de desenvolvimento concluído: {Transaction.objects.count()} transações fictícias."))
