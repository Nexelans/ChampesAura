# Fichier: app/schemas.py
# Définit les modèles de données Pydantic pour la validation des requêtes/réponses API.

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

# --- Schémas de base et de création ---

class PlayerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    handicap: float

class PlayerCreate(PlayerBase):
    team_id: Optional[int] = None # Permet d'assigner une équipe à la création

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    captain_id: int

class CompetitionBase(BaseModel):
    name: str
    date: date

class CompetitionCreate(CompetitionBase):
    pass

class ScoreBase(BaseModel):
    points: int

class ScoreCreate(ScoreBase):
    player_id: int
    competition_id: int


# --- Schémas de lecture (pour les réponses API) ---
# L'ordre est important pour que les références de type fonctionnent.
# Nous définissons les schémas de base avant ceux qui les utilisent.

class Team(TeamBase):
    id: int
    captain_id: int

    class Config:
        from_attributes = True

class Player(PlayerBase):
    id: int
    team: Optional[Team] = None # Affiche les détails de l'équipe du joueur

    class Config:
        from_attributes = True

class Score(ScoreBase):
    id: int
    player_id: int
    competition_id: int

    class Config:
        from_attributes = True

class Competition(CompetitionBase):
    id: int
    scores: List[Score] = []

    class Config:
        from_attributes = True
        
# Maintenant que Player est défini, on peut créer un schéma Team détaillé.
class TeamDetails(Team):
    captain: Player
    members: List[Player] = []

