# Fichier: app/routers/competitions.py
# Définit les routes API pour la ressource "competitions".

from typing import List
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/competitions",
    tags=["Competitions"],
)


@router.post("/", response_model=schemas.Competition, status_code=status.HTTP_201_CREATED)
def create_competition(competition: schemas.CompetitionCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle compétition.
    """
    return crud.create_competition(db=db, competition=competition)


@router.get("/", response_model=List[schemas.Competition])
def read_competitions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère une liste de toutes les compétitions.
    """
    competitions = crud.get_competitions(db, skip=skip, limit=limit)
    return competitions


@router.get("/{competition_id}", response_model=schemas.Competition)
def read_competition(competition_id: int, db: Session = Depends(get_db)):
    """
    Récupère les détails d'une compétition spécifique par son ID.
    """
    db_competition = crud.get_competition(db, competition_id=competition_id)
    if db_competition is None:
        raise HTTPException(status_code=404, detail="Compétition non trouvée.")
    return db_competition
