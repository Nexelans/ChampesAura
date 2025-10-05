# Fichier: app/crud.py
# Contient les fonctions pour interagir avec la base de données.

from sqlalchemy.orm import Session

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

# --- Fonctions CRUD pour les Compétitions (à venir) ---
# ...

# --- Fonctions CRUD pour les Scores (à venir) ---
# ...
