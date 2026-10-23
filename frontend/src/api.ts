import type { Page, Summary, Transaction, Level } from './types';
const base = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api';
async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${base}${path}`, { ...options, headers: { 'Content-Type': 'application/json', ...options?.headers } });
  if (!response.ok) { let message = `Erro ${response.status}`; try { const body = await response.json(); message = body.mensagem || body.detail || message; } catch { /* response without JSON */ } throw new Error(message); }
  return response.json() as Promise<T>;
}
export const getSummary = () => request<Summary>('/dashboard/summary');
export const getTransactions = (page = 1, risk?: Level) => request<Page<Transaction>>(`/transactions?page=${page}${risk ? `&risk_level=${risk}` : ''}&ordering=-occurred_at`);
export const getTransaction = (id: string) => request<Transaction>(`/transactions/${id}`);
export const simulateTransaction = () => request<Transaction>('/transactions/simulate', { method: 'POST', body: '{}' });
