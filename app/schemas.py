# Fichier: app/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import List, Optional


# --- Player Schemas ---
class PlayerBase(BaseModel):
    name: str
    handicap: float


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int

    class Config:
        from_attributes = True


# --- Competition Schemas ---
class CompetitionBase(BaseModel):
    name: str
    date: date
    location: Optional[str] = None
    format: Optional[str] = None


class CompetitionCreate(CompetitionBase):
    pass


class Competition(CompetitionBase):
    id: int

    class Config:
        from_attributes = True


# --- Score Schemas ---
class ScoreBase(BaseModel):
    gross_score: int
    net_score: float
    player_id: int
    competition_id: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int

    class Config:
        from_attributes = True

