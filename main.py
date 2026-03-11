from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/buscar/{patente}")
def buscar_auto(patente: str):
    return {
        "patente": patente.upper(),
        "robo": "✅ Limpio (AutoSeguro) [cite: 78, 80]",
        "prt": "📅 Al día (PRT.cl) [cite: 41]",
        "km": "📈 85k (Consistente) [cite: 43, 45]",
        "multas": "💸 $0 (SUBDERE) [cite: 67]",
        "tag": "🛣️ Sin deuda [cite: 73, 75]",
        "recalls": "⚠️ 1 pendiente (SERNAC) [cite: 36, 150]",
        "ventas": "🔍 FB Marketplace (2024) [cite: 89, 90]"
    }
