from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Este es el "Pase VIP" que deja que tu WordPress se conecte al robot
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/buscar/{patente}")
def buscar_patente(patente: str):
    return {
        "patente": patente.upper(),
        "Carabineros_Robo": random.choice(["Limpio", "Alerta"]),
        "PRT_Revision": random.choice(["Aprobada", "Rechazada"]),
        "MTT_Transporte": random.choice(["Particular", "Ex-Taxi"])
    }