# Fichier: app/main.py
# Point d'entrée de l'application FastAPI (version mise à jour).

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import SessionLocal, engine, get_db
from .routers import players, competitions  # <--- NOUVEL IMPORT

# Crée les tables dans la base de données (si elles n'existent pas)
# Attention : dans un environnement de production plus avancé, on utiliserait Alembic pour les migrations.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestion de Compétitions de Golf",
    description="Une API pour gérer les joueurs, les compétitions et les scores de golf.",
    version="0.1.0",
)

# Inclusion des routeurs
app.include_router(players.router)
app.include_router(competitions.router) # <--- NOUVELLE LIGNE


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint racine de l'API.
    """
    return {"message": "Bienvenue sur l'API de gestion de compétitions de golf !"}

