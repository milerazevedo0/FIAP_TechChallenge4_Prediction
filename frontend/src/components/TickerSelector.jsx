import React from "react";

export default function TickerSelector({ tickers = [], value, onChange, disabled=false, className = "" }) {
  return (
    <select
      className={className}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      disabled={disabled}
    >
      <option value="">{ disabled ? "Carregando..." : "Selecione uma ação" }</option>
      {tickers.map((t, i) => {
        // t pode ser string ou objeto { ticker, name }
        const tickerVal = typeof t === "string" ? t : t.ticker;
        const label = typeof t === "string" ? t : `${t.ticker} — ${t.name ?? ""}`;
        return <option key={i} value={tickerVal}>{label}</option>;
      })}
    </select>
  );
}
