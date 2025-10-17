from typing import List
import investpy
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockProvider:
    """
    Classe que encapsula as integrações externas: investpy (lista de ativos) e yfinance (dados historicos).
    """

    def get_tickers_by_market(self, market: str) -> List[dict]:
        """
        market: 'br' or 'us'
        retorna lista de dicts {'ticker': 'PETR4.SA', 'name': 'PETROBRAS'}
        """
        if market.lower() in ("br", "brazil", "brasil"):
            # exemplo usando investpy para BR
            df = investpy.stocks.get_stocks(country='brazil')  # retorna DataFrame
            # a coluna 'symbol' ou 'ticker' pode variar; adapte conforme versão
            items = []
            for _, row in df.iterrows():
                # investpy geralmente tem 'symbol' ou 'ticker'
                symbol = row.get('symbol') or row.get('ticker') or row.get('isin')
                name = row.get('name') or row.get('company') or None
                if symbol:
                    # no B3 frequentemente o ticker precisa de .SA (depende da fonte)
                    items.append({'ticker': symbol, 'name': name})
            return items

        elif market.lower() in ("us", "usa", "america"):
            # Para US, investpy também pode ter, mas podemos usar yfinance para validar
            # vamos buscar um conjunto reduzido ou usar investpy country='united states'
            df = investpy.stocks.get_stocks(country='united states')
            items = []
            for _, row in df.iterrows():
                symbol = row.get('symbol') or row.get('ticker')
                name = row.get('name')
                if symbol:
                    items.append({'ticker': symbol, 'name': name})
            return items
        else:
            return []

    def get_quote(self, ticker: str, days: int = 30) -> dict:
        """
        Busca metadados e histórico dos últimos `days` dias usando yfinance.
        Retorna dicionário compatível com QuoteResponse.
        """
        tk = yf.Ticker(ticker)
        info = tk.info or {}
        # historical data: period 30d or start/end
        hist = tk.history(period=f"{days}d", interval="1d", auto_adjust=False)
        hist = hist.reset_index()  # coluna Date
        prices = []
        for _, r in hist.iterrows():
            prices.append({
                "date": r["Date"].strftime("%Y-%m-%d"),
                "open": float(r["Open"]),
                "high": float(r["High"]),
                "low": float(r["Low"]),
                "close": float(r["Close"]),
                "volume": int(r["Volume"])
            })
        return {
            "ticker": ticker,
            "name": info.get("shortName") or info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "prices": prices
        }
