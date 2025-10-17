# Tech Challenge fase 4

Este projeto é uma aplicação completa com **FastAPI** (backend) e **React** (frontend) que permite consultar informações sobre ações brasileiras e americanas.

---

## 🚀 Funcionalidades

- Seleção de mercado (Brasil / EUA)
- Listagem dinâmica de ações conforme o mercado escolhido
- Consulta de dados da ação (nome, segmento, ticker)
- Exibição de gráfico com os preços dos últimos 30 dias
- Arquitetura limpa e orientada a objetos

---

## 🧩 Estrutura do Projeto

```
FIAP_TechChallenge4_Prediction/
│
├── backend/
│   ├── backend/
│   │   ├── api/
│   │   │   └── routers/
│   │   │       ├── markets.py
│   │   │       └── quotes.py
│   │   ├── schemas/
│   │   │   └── stock.py
│   │   ├── services/
│   │   │   └── stock_provider.py
│   │   ├── utils/
│   │   │   └── date_utils.py
│   │   └── main.py
│   ├── pyproject.toml
│   ├── static/
│   └── tests/
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── MarketSelector.jsx
    │   │   ├── QuoteResult.jsx
    │   │   └── TickerSelector.jsx
    │   ├── App.jsx
    │   └── main.jsx
    ├── package.json
    ├── vite.config.js
    └── index.html
```

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/milerazevedo0/FIAP_TechChallenge4_Prediction.git
cd FIAP_TechChallenge4_Prediction
```

---

### 2️⃣ Backend (FastAPI + Poetry)

Se você não tem o Poetry instalado, instale seguindo as instruções em https://python-poetry.org/docs/#installation

**Instalar dependências e ativar um shell com o ambiente do Poetry:**

```bash
cd backend
poetry install
poetry shell
```

> Alternativa: para executar sem entrar no shell, use `poetry run <comando>` (ex.: `poetry run uvicorn app.main:app --reload`).

**Rodar o servidor FastAPI:**

```bash
poetry run uvicorn app.main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`  
A documentação automática do FastAPI estará em: `http://127.0.0.1:8000/docs`

---

### 3️⃣ Frontend (React + Vite)

Abra outro terminal:
```bash
cd frontend
npm install
npm run dev
```

O frontend será iniciado em: [http://localhost:5173](http://localhost:5173)

> Se preferir servir o frontend pelo backend em produção, gere o build (`npm run build`) e copie o conteúdo de `dist/` para a pasta `backend/static` (ou ajuste a configuração do FastAPI para servir os arquivos estáticos).

---

## 🧠 Tecnologias Utilizadas

**Backend:**
- Python
- FastAPI
- Uvicorn
- Poetry (gerenciamento de dependências)
- Pydantic
- yfinance
- Pydantic

**Frontend:**
- React
- Vite
- Chart.js

---

## 🧰 Próximos Passos

- Adicionar Docker
- Adicionar cache de resultados

---

## 🧑‍💻 Autor

- **Miler Azevedo**  
📧 [GitHub](https://github.com/milerazevedo0)
- **Arthur**
- **Murilo**
- **Kaio**

---

> Este projeto faz parte do aprendizado prático sobre integração entre **APIs**, **FastAPI**, **React**, e **serviços externos de dados financeiros**.
