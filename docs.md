PIXPROTECT
Simulador de detecção de transações suspeitas


COMO USAR COM A IA

Cole este documento inteiro e peça: construa o projeto completo de uma vez, sem me fazer perguntas. Onde faltar detalhe, decida e anote a decisão no README. Siga os contratos de API ao pé da letra, escreva os testes listados e entregue com um comando de seed que popule tudo.


A IDEIA EM DUAS LINHAS

Painel de análise de transações PIX fictícias. Cada transação que chega recebe um Risk Score de 0 a 100, e o sistema guarda não só o número, mas o motivo de cada ponto.


O QUE TIRA ISSO DO NÍVEL DE INICIANTE

O score é calculado por uma função pura, sem tocar no banco, e cada transação guarda a lista de razões que gerou o resultado (regra, pontos, detalhe). Um score sem explicação é caixa-preta. Com explicação, a tela de detalhe mostra exatamente por que aquele PIX foi marcado como risco alto, e é isso que parece sistema antifraude de verdade.


STACK

Backend: Python 3.12, Django 5, Django REST Framework, django-filter, django-cors-headers
Banco: PostgreSQL 16 (docker compose só com o banco, para facilitar)
Frontend: React + TypeScript + Vite + Recharts


ESTRUTURA DE PASTAS

pixprotect/
  docker-compose.yml                        só o postgres
  backend/config/settings.py
  backend/transactions/models.py
  backend/transactions/scoring.py           função pura, sem acesso ao banco
  backend/transactions/services.py          busca histórico, chama o scoring, salva com transaction.atomic
  backend/transactions/serializers.py
  backend/transactions/views.py
  backend/transactions/filters.py
  backend/transactions/urls.py
  backend/transactions/tests/test_scoring.py
  backend/transactions/tests/test_api.py
  backend/transactions/management/commands/seed_pix.py
  frontend/src/pages/Dashboard.tsx
  frontend/src/pages/TransactionList.tsx
  frontend/src/pages/TransactionDetail.tsx
  frontend/src/components/RiskBadge.tsx
  frontend/src/components/ScoreMeter.tsx
  frontend/src/api.ts
  frontend/src/types.ts


MODELO DE DADOS

Transaction:
  codigo (inteiro único, aparece como PIX #83921)
  valor (Decimal 12,2. Nunca float para dinheiro)
  occurred_at (datetime com fuso)
  conta_origem (texto), cidade_origem, uf_origem
  chave_destino, nome_destino, cidade_destino, uf_destino
  risk_score (inteiro, 0 a 100)
  risk_level (baixo, medio, alto)
  reasons (JSONField: lista de { regra, pontos, detalhe })
  created_at
Índices em (conta_origem, occurred_at) e em risk_score.
risk_score, risk_level e reasons são somente leitura na API. O cliente nunca informa o score.


REGRAS DE SCORE

valor acima de R$ 5.000,00                       +30
valor acima de R$ 2.000,00 até R$ 5.000,00       +15
horário de 00:00 até 04:59                       +20
destinatário novo                                +25
rajada: 4 ou mais transações da mesma conta
nos 10 minutos anteriores                        +15
estado de origem diferente do de destino         +10

As duas faixas de valor são exclusivas entre si. Com isso o máximo possível é exatamente 100.
Destinatário novo: nenhuma transação anterior da mesma conta_origem para a mesma chave_destino.
Janela da rajada: de occurred_at menos 10 minutos (inclusive) até occurred_at (exclusive).
Histórico sempre usa occurred_at da transação, nunca a hora em que ela foi gravada. Só conta o que veio antes dela. Isso mantém o seed e o reprocessamento consistentes.

Níveis: de 0 a 39 baixo, de 40 a 69 médio, de 70 a 100 alto.

Assinatura da função pura:
score_transaction(tx, historico) devolve (score, nivel, reasons)
onde tx é um dict com valor, occurred_at, conta, chave_destino e UFs, e historico é uma lista simples de (chave_destino, occurred_at) da mesma conta. Sem ORM dentro dela.

Exemplo para a documentação e para o teste:
PIX #83921
Valor: R$ 4.850,00 (+15)
Horário: 03:17 (+20)
Origem Recife PE, destino São Paulo SP (+10)
Destinatário novo (+25)
Sem rajada (0)
RISK SCORE: 70/100, nível alto


CONTRATO DA API

POST  /api/transactions
      recebe os dados, calcula o score, salva e devolve 201 com score, nível e reasons
GET   /api/transactions?risk_level=alto&min_score=60&conta=&ordering=-occurred_at&page=1
      paginado, 20 por página
GET   /api/transactions/{id}
GET   /api/dashboard/summary
      total, contagem por nível, valor_total_alto_risco, por_hora (24 buckets com quantidade e score médio)
POST  /api/transactions/simulate
      gera uma transação aleatória plausível, pontua e devolve. É o botão de demonstração.

Erros no formato { erro, mensagem }. Validação: valor maior que zero, UF com 2 letras, chave_destino obrigatória.


TELAS

Dashboard: quatro cards (total, alto risco, valor sob risco alto, score médio), gráfico de barras por nível e gráfico de linha por hora. Botão Gerar transação de teste.
Lista: chips de filtro Todos, Baixo, Médio, Alto. Tabela com código, valor formatado em pt-BR com Intl.NumberFormat, horário, origem para destino, badge de risco e score. Clique abre o detalhe.
Detalhe: cabeçalho no formato do exemplo, medidor de 0 a 100 e a lista de razões, cada uma como +25 Destinatário novo: nunca enviou para esta chave. Mostra também as transações dessa conta nos 10 minutos anteriores.

Badge sempre leva texto (Baixo, Médio, Alto), não só cor.


DADOS DE SEED (comando seed_pix)

15 contas, cerca de 250 transações nos últimos 14 dias, geradas em ordem cronológica e passando pelo mesmo serviço de score. Nunca grave score na mão. A maioria com valores baixos e em horário comercial, cerca de 8% suspeitas (madrugada, valor alto, destino novo e em outro estado). A PIX 83921 do exemplo entra por último, explicitamente.


ORDEM DE CONSTRUÇÃO

passo 1: docker compose, settings, model e migrations
passo 2: scoring.py com testes
passo 3: services.py, serializers, views, filtros e urls
passo 4: seed_pix
passo 5: frontend


TESTES OBRIGATÓRIOS

Cada regra isolada, uma por teste.
Limites de valor: 2.000,00 pontua 0; 2.000,01 pontua 15; 5.000,00 pontua 15; 5.000,01 pontua 30.
Limites de horário: 04:59 pontua, 05:00 não pontua.
Janela da rajada: 3 transações anteriores não pontuam, 4 pontuam, uma exatamente 10 minutos atrás entra e uma a 10 minutos e 1 segundo fica fora.
Combinação máxima dá 100, nunca mais.
PIX 83921 dá 70 com quatro razões.
POST na API ignora score enviado pelo cliente.


O QUE PRECISA ESTAR LÁ PARA PARECER INTERMEDIÁRIO

Função pura separada da camada de banco. Decimal para dinheiro. Razões persistidas. Testes nos limites. Serializers com validação. django-filter e paginação. Índices pensados para a consulta de histórico.


FORA DO ESCOPO

Login, integração real com o Pix, machine learning, bloqueio de conta. Uma tela para editar os pesos das regras é um bom extra para depois.


PRONTO QUANDO

O POST com os dados da PIX 83921 devolve score 70, nível alto e quatro razões somando 70. A lista filtra por Alto, o detalhe mostra o motivo de cada ponto e o botão Gerar transação de teste faz uma nova linha aparecer já pontuada.