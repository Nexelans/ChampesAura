# Fichier: app/crud.py
# Contient les fonctions pour interagir avec la base de données.

from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas


# --- Fonctions CRUD pour les Joueurs (Player) ---

def get_player(db: Session, player_id: int):
    """
    Récupère un joueur par son ID.
    """
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_player_by_email(db: Session, email: str):
    """
    Récupère un joueur par son adresse e-mail.
    """
    return db.query(models.Player).filter(models.Player.email == email).first()


def get_players(db: Session, skip: int = 0, limit: int = 100):
    """
    Récupère une liste de joueurs avec pagination.
    """
    return db.query(models.Player).offset(skip).limit(limit).all()


def create_player(db: Session, player: schemas.PlayerCreate):
    """
    Crée un nouveau joueur dans la base de données.
    """
    db_player = models.Player(
        first_name=player.first_name,
        last_name=player.last_name,
        email=player.email,
        handicap=player.handicap
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


# --- Fonctions CRUD pour les Compétitions (Competition) ---

def get_competition(db: Session, competition_id: int):
    """
    Récupère une compétition par son ID.
    """
    return db.query(models.Competition).filter(models.Competition.id == competition_id).first()


def get_competitions(db: Session, skip: int = 0, limit: int = 100):
    """
    Récupère une liste de compétitions avec pagination.
    """
    return db.query(models.Competition).offset(skip).limit(limit).all()


def create_competition(db: Session, competition: schemas.CompetitionCreate):
    """
    Crée une nouvelle compétition.
    """
    db_competition = models.Competition(
        name=competition.name,
        date=competition.date
    )
    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition


# --- Fonctions CRUD pour les Scores (Score) ---

def get_scores(db: Session, skip: int = 0, limit: int = 100):
    """
    Récupère une liste de tous les scores.
    """
    return db.query(models.Score).offset(skip).limit(limit).all()


def create_score(db: Session, score: schemas.ScoreCreate, player_id: int, competition_id: int):
    """
    Crée un nouveau score pour un joueur dans une compétition.
    """
    db_score = models.Score(
        points=score.points,
        player_id=player_id,
        competition_id=competition_id
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

