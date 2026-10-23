# PIXPROTECT

Painel demonstrativo de análise de risco para transações PIX, com score explicável, dashboard, feed e detalhe.

## Execução local

1. API (Python 3.12+): `python -m pip install -r requirements.txt`
2. Em `backend/`: `python manage.py migrate`, `python manage.py seed_pix` e `python manage.py runserver`
3. Frontend: em `frontend/`, execute `npm install` e `npm run dev`
4. Abra `http://localhost:5173`.

O backend usa SQLite automaticamente para desenvolvimento. Para PostgreSQL, inicie o serviço com `docker compose up -d` na raiz e configure `DATABASE_URL` conforme `.env.example`. O frontend aceita `VITE_API_URL`; por padrão usa `http://localhost:8000/api`.

## Dados de demonstração

`python manage.py seed_pix` substitui os registros existentes por 250 transações fictícias, incluindo PIX #83921 com score 70. O botão “Gerar transação de teste” também cria um registro fictício pela API. Ambos são identificados na interface; POSTs normais permanecem marcados como dados não demonstrativos.

## API

- `GET /api/dashboard/summary`
- `GET|POST /api/transactions`
- `GET /api/transactions/{id}`
- `POST /api/transactions/simulate`

Não há integração com o sistema Pix, autenticação ou ação bancária real.
