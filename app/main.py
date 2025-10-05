# Fichier: app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import SessionLocal, engine, get_db

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestionnaire de Compétitions de Golf",
    description="Une application pour gérer les joueurs, les compétitions et les scores.",
    version="0.1.0"
)


@app.get("/", tags=["Root"])
def read_root():
    """
    Welcome endpoint.
    """
    return {"message": "Bienvenue sur l'application de gestion de compétitions de golf !"}


# --- CRUD Operations and Endpoints will be added here ---

# Example: Placeholder for creating a player
# @app.post("/players/", response_model=schemas.Player, tags=["Players"])
# def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
#     # Logic to create a player will go here
#     return {"message": "Player creation logic to be implemented"}

