from decimal import Decimal

def score_transaction(tx, historico):
    """Pure PIX risk scoring. historico is [(chave_destino, occurred_at), ...]."""
    score = 0
    reasons = []
    def add(regra, pontos, detalhe):
        nonlocal score
        score += pontos
        reasons.append({"regra": regra, "pontos": pontos, "detalhe": detalhe})

    value = Decimal(str(tx["valor"]))
    if value > Decimal("5000.00"):
        add("Valor acima de R$ 5.000,00", 30, f"O valor de R$ {value:.2f} excede R$ 5.000,00.")
    elif value > Decimal("2000.00"):
        add("Valor acima de R$ 2.000,00", 15, f"O valor de R$ {value:.2f} excede R$ 2.000,00.")

    occurred_at = tx["occurred_at"]
    if 0 <= occurred_at.hour < 5:
        add("Horário entre 00:00 e 04:59", 20, f"Transação realizada às {occurred_at:%H:%M}.")

    if not any(key == tx["chave_destino"] for key, _ in historico):
        add("Destinatário novo", 25, "Não há transferência anterior desta conta para esta chave.")

    start = occurred_at - __import__("datetime").timedelta(minutes=10)
    burst = sum(1 for _, previous_at in historico if start <= previous_at < occurred_at)
    if burst >= 4:
        add("Rajada de transações", 15, f"{burst} transações da mesma conta nos 10 minutos anteriores.")

    if tx["uf_origem"].upper() != tx["uf_destino"].upper():
        add("Estados diferentes", 10, f"Origem {tx['uf_origem']} e destino {tx['uf_destino']}.")

    score = min(score, 100)
    level = "baixo" if score < 40 else "medio" if score < 70 else "alto"
    return score, level, reasons
