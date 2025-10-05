# Fichier: app/routers/players.py
# Définit les routes API pour la ressource "players".

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import get_db

# Création d'un "router" qui sera inclus dans l'application principale
router = APIRouter(
    prefix="/players",  # Toutes les routes de ce fichier commenceront par /players
    tags=["Players"],     # Groupe les routes dans la documentation de l'API
)


@router.post("/", response_model=schemas.Player, status_code=status.HTTP_201_CREATED)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau joueur.
    Vérifie si un joueur avec le même email existe déjà.
    """
    db_player = crud.get_player_by_email(db, email=player.email)
    if db_player:
        raise HTTPException(status_code=400, detail="Un joueur avec cet email existe déjà.")
    return crud.create_player(db=db, player=player)


@router.get("/", response_model=List[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère une liste de tous les joueurs.
    """
    players = crud.get_players(db, skip=skip, limit=limit)
    return players


@router.get("/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    """
    Récupère les détails d'un joueur spécifique par son ID.
    """
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Joueur non trouvé.")
    return db_player
