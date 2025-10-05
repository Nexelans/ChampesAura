# Fichier: app/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from .database import Base


class Competition(Base):
    """
    Represents a golf competition.
    """
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String)
    format = Column(String)  # e.g., "Stroke Play", "Stableford"

    # Relationship to scores
    scores = relationship("Score", back_populates="competition")


class Player(Base):
    """
    Represents a golf player.
    """
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    handicap = Column(Float, nullable=False)

    # Relationship to scores
    scores = relationship("Score", back_populates="player")


class Score(Base):
    """
    Represents a player's score in a specific competition.
    """
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    gross_score = Column(Integer, nullable=False)
    net_score = Column(Float, nullable=False)

    # Foreign keys
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)

    # Relationships
    player = relationship("Player", back_populates="scores")
    competition = relationship("Competition", back_populates="scores")

