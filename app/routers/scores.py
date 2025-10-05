# Fichier: app/routers/scores.py
# Définit les routes API pour la ressource "scores".

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/scores",
    tags=["Scores"],
)


@router.post("/", response_model=schemas.Score, status_code=status.HTTP_201_CREATED)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau score pour un joueur dans une compétition.

    - **player_id**: ID du joueur qui a réalisé le score.
    - **competition_id**: ID de la compétition dans laquelle le score a été réalisé.
    - **points**: Le nombre de points obtenus.
    """
    # Vérifier que le joueur et la compétition existent avant de créer le score
    db_player = crud.get_player(db, player_id=score.player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail=f"Le joueur avec l'ID {score.player_id} n'a pas été trouvé.")
    
    db_competition = crud.get_competition(db, competition_id=score.competition_id)
    if not db_competition:
        raise HTTPException(status_code=404, detail=f"La compétition avec l'ID {score.competition_id} n'a pas été trouvée.")

    return crud.create_score(db=db, score=score, player_id=score.player_id, competition_id=score.competition_id)


@router.get("/", response_model=List[schemas.Score])
def read_scores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère une liste de tous les scores.
    """
    scores = crud.get_scores(db, skip=skip, limit=limit)
    return scores
