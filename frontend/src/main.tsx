import React from 'react';
import { createRoot } from 'react-dom/client';
import Dashboard from './pages/Dashboard';
import TransactionList from './pages/TransactionList';
import TransactionDetail from './pages/TransactionDetail';
import { Shell } from './components/Shell';
import './styles.css';
function App(){const [route,setRoute]=React.useState(location.hash.slice(1)||'dashboard');React.useEffect(()=>{const sync=()=>setRoute(location.hash.slice(1)||'dashboard');window.addEventListener('hashchange',sync);return()=>window.removeEventListener('hashchange',sync);},[]);const isDetail=route.startsWith('transacao/');const page=isDetail?'detail':route==='transacoes'?'transactions':'dashboard';return <Shell page={page}>{isDetail?<TransactionDetail id={route.split('/')[1]}/>:page==='transactions'?<TransactionList/>:<Dashboard/>}</Shell>}
createRoot(document.getElementById('root')!).render(<React.StrictMode><App/></React.StrictMode>);
