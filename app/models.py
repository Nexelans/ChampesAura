# Fichier: app/models.py
# Définit les tables et les relations de la base de données avec SQLAlchemy.
import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship, Mapped

from .database import Base

# La table d'association plusieurs-à-plusieurs a été supprimée.

class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = Column(Integer, primary_key=True)
    first_name: Mapped[str] = Column(String, index=True)
    last_name: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    handicap: Mapped[float] = Column(Float, index=True)

    # NOUVEAU : Clé étrangère vers l'équipe du joueur.
    # Un joueur appartient à une seule équipe (ou à aucune).
    team_id: Mapped[int] = Column(Integer, ForeignKey("teams.id"), nullable=True)

    # Relation vers les scores du joueur (inchangée)
    scores: Mapped["Score"] = relationship("Score", back_populates="player")
    
    # MIS A JOUR : Relation vers l'équipe du joueur.
    team: Mapped["Team"] = relationship("Team", back_populates="members")
    
    # La relation "captained_team" est supprimée d'ici pour simplifier. 
    # On sait si un joueur est capitaine via la table Team.


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, index=True, unique=True)
    
    # Clé étrangère vers le joueur qui est le capitaine.
    # unique=True garantit qu'un joueur ne peut être capitaine que d'une seule équipe.
    captain_id: Mapped[int] = Column(Integer, ForeignKey("players.id"), unique=True)

    # Relation vers l'objet Player du capitaine.
    # C'est une relation simple, sans retour, pour récupérer les infos du capitaine.
    captain: Mapped["Player"] = relationship("Player", foreign_keys=[captain_id])
    
    # MIS A JOUR : Relation vers la liste des joueurs membres de l'équipe.
    members: Mapped["Player"] = relationship(
        "Player", back_populates="team", foreign_keys="[Player.team_id]"
    )


class Competition(Base):
    __tablename__ = "competitions"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, index=True)
    date: Mapped[datetime.date] = Column(Date, index=True)

    # Relation vers les scores de la compétition (inchangée)
    scores: Mapped["Score"] = relationship("Score", back_populates="competition")


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = Column(Integer, primary_key=True)
    points: Mapped[int] = Column(Integer)
    
    player_id: Mapped[int] = Column(Integer, ForeignKey("players.id"))
    competition_id: Mapped[int] = Column(Integer, ForeignKey("competitions.id"))

    # Relations vers les objets Player et Competition (inchangées)
    player: Mapped["Player"] = relationship("Player", back_populates="scores")
    competition: Mapped["Competition"] = relationship("Competition", back_populates="scores")

