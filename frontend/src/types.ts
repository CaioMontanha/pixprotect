export type Level = 'baixo' | 'medio' | 'alto';
export interface Reason { regra: string; pontos: number; detalhe: string }
export interface Transaction { id: number; codigo: number; valor: string; occurred_at: string; conta_origem: string; cidade_origem: string; uf_origem: string; chave_destino: string; nome_destino: string; cidade_destino: string; uf_destino: string; risk_score: number; risk_level: Level; reasons: Reason[]; anteriores_10_minutos: {codigo:number;valor:string;occurred_at:string;nome_destino:string}[]; is_demo: boolean }
export interface Summary { total: number; por_nivel: Record<Level, number>; valor_total_alto_risco: string; score_medio: number; dados_demonstracao: boolean; por_hora: { hora: number; quantidade: number; score_medio: number }[] }
export interface Page<T> { count: number; next: string | null; previous: string | null; results: T[] }
