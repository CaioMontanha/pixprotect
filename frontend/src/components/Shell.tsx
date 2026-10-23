import { LayoutDashboard, ReceiptText, Menu, X } from 'lucide-react';
import { useState } from 'react';
export function Shell({ children, page }: { children: React.ReactNode; page: string }) {
  const [open, setOpen] = useState(false);
  return <div className="app-shell">
    {open && <button className="scrim" aria-label="Fechar menu" onClick={() => setOpen(false)} />}
    <aside className={`sidebar ${open ? 'sidebar-open' : ''}`}>
      <a className="brand" href="#dashboard"><span className="brand-icon"><img src="/logo-montanha.png" alt="Logo Montanha"/></span><span><b>PIXPROTECT <small>v1.0</small></b><em>Prevenção de Fraude PIX</em></span></a>
      <nav aria-label="Navegação principal"><a className={page === 'dashboard' ? 'active' : ''} href="#dashboard" onClick={() => setOpen(false)}><LayoutDashboard size={19}/>Dashboard</a><a className={page !== 'dashboard' ? 'active' : ''} href="#transacoes" onClick={() => setOpen(false)}><ReceiptText size={19}/>Transações</a></nav>
      <div className="sidebar-bottom"><span className="online-dot"/> Ambiente: API conectada</div>
    </aside>
    <main className="main-area"><header className="topbar"><button className="menu-toggle icon-button" onClick={() => setOpen(!open)} aria-label={open ? 'Fechar navegação' : 'Abrir navegação'} aria-expanded={open}>{open ? <X/> : <Menu/>}</button><div className="topbar-status"><i/> Motor heurístico <b>·</b> {import.meta.env.VITE_API_URL ? 'Conectado' : 'API localhost:8000'}</div><div className="profile"><div className="avatar">AR</div><div><b>Analista de Risco</b><span>Operações antifraude</span></div></div></header>{children}<footer className="app-footer"><span><i/> Motor de regras PIXPROTECT</span><span>Dados fornecidos pela API configurada</span></footer></main>
    <a className="portfolio-launcher" href="https://caio-montanha.vercel.app/" target="_blank" rel="noreferrer" aria-label="Abrir meu portfólio em uma nova aba" title="Meu portfólio"><span className="portfolio-mark" aria-hidden="true"><img src="/logo-montanha.png" alt=""/></span><span>Portfólio</span></a>
  </div>;
}
