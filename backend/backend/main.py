from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routers import markets, quotes

app = FastAPI(title="Stocks API")

# CORS - em dev permitir localhost:5173 (Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção restringir
    allow_methods=["*"],
    allow_headers=["*"],
)

# incluir routers
app.include_router(markets.router, prefix="/api", tags=["markets"])
app.include_router(quotes.router, prefix="/api", tags=["quotes"])

# montar o build do react (após `npm run build` em frontend -> copia para backend/static)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# Para iniciar a aplicação uvicorn backend.main:app --reload