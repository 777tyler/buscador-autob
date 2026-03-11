from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Esto permite que tu WordPress se comunique con el servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "Servidor de Auto B funcionando"}

@app.get("/buscar/{patente}")
def buscar_auto(patente: str):
    # Datos de prueba para tu marketplace
    datos_falsos = {
        "patente": patente.upper(),
        "Carabineros_Robo": "Sin encargo vigente",
        "PRT_Revision": "Al día (Vence Oct 2026)",
        "MTT_Transporte": "Particular (Auto bueno y andando)"
    }
    return datos_falsos
    # ... (Mantén la lógica de FastAPI y CORS igual)
@app.get("/buscar/{patente}")
def buscar_auto(patente: str):
    return {
        "patente": patente.upper(),
        "robo": "✅ Limpio (Sin encargo)",
        "prt": "📅 Al día (Vence Oct 2026)",
        "km": "📈 Historial: 85.000 km (Consistente)",
        "tag": "💸 Deuda TAG: $0 (Sin pendientes)",
        "recalls": "⚠️ 1 pendiente (Falla Airbag)",
        "ventas": "🔍 Hallada en Facebook (2024) - $7.2M"
    }
# ... (Mantén la lógica de FastAPI y CORS igual)
@app.get("/buscar/{patente}")
def buscar_auto(patente: str):
    return {
        "patente": patente.upper(),
        "robo": "✅ Limpio (Sin encargo)",
        "prt": "📅 Al día (Vence Oct 2026)",
        "km": "📈 Historial: 85.000 km (Consistente)",
        "tag": "💸 Deuda TAG: $0 (Sin pendientes)",
        "recalls": "⚠️ 1 pendiente (Falla Airbag)",
        "ventas": "🔍 Hallada en Facebook (2024) - $7.2M"
    }
