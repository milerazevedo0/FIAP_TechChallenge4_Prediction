from pydantic import BaseModel
from typing import List, Optional

class MarketList(BaseModel):
    markets: List[str]

class TickerItem(BaseModel):
    ticker: str
    name: Optional[str]

class TickerList(BaseModel):
    market: str
    tickers: List[TickerItem]

class QuoteRequest(BaseModel):
    ticker: str

class PricePoint(BaseModel):
    date: str  # ISO
    open: float
    high: float
    low: float
    close: float
    volume: int

class QuoteResponse(BaseModel):
    ticker: str
    name: Optional[str]
    sector: Optional[str]
    industry: Optional[str]
    prices: List[PricePoint]  # últimos 30 dias
