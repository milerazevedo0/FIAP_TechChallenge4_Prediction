import React from "react";

export default function MarketSelector({ value, onChange, className = "" }) {
  return (
    <select
      className={className}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    >
      <option value="">Selecione</option>
      <option value="br">Ações Brasileiras</option>
      <option value="us">Ações Americanas</option>
    </select>
  );
}
