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


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = Column(Integer, primary_key=True)
    first_name: Mapped[str] = Column(String, index=True)
    last_name: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    handicap: Mapped[float] = Column(Float, index=True)

    team_id: Mapped[int] = Column(Integer, ForeignKey("teams.id"), nullable=True)

    scores: Mapped["Score"] = relationship("Score", back_populates="player")
    
    # CORRECTION : Ajout de l'argument 'foreign_keys' pour lever l'ambiguïté.
    team: Mapped["Team"] = relationship(
        "Team", back_populates="members", foreign_keys=[team_id]
    )


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, index=True, unique=True)
    
    captain_id: Mapped[int] = Column(Integer, ForeignKey("players.id"), unique=True)

    # La relation 'captain' n'a pas d'ambiguïté, elle est correcte.
    captain: Mapped["Player"] = relationship("Player", foreign_keys=[captain_id])
    
    # La relation 'members' était déjà correcte, mais je la garde pour la cohérence.
    members: Mapped[list["Player"]] = relationship(
        "Player", back_populates="team", foreign_keys="[Player.team_id]"
    )


class Competition(Base):
    __tablename__ = "competitions"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String, index=True)
    date: Mapped[datetime.date] = Column(Date, index=True)

    scores: Mapped["Score"] = relationship("Score", back_populates="competition")


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = Column(Integer, primary_key=True)
    points: Mapped[int] = Column(Integer)
    
    player_id: Mapped[int] = Column(Integer, ForeignKey("players.id"))
    competition_id: Mapped[int] = Column(Integer, ForeignKey("competitions.id"))

    player: Mapped["Player"] = relationship("Player", back_populates="scores")
    competition: Mapped["Competition"] = relationship("Competition", back_populates="scores")
```

### Ce que j'ai changé :

Dans le fichier `app/models.py`, sur le modèle `Player`, j'ai modifié la relation `team` pour y inclure `foreign_keys=[team_id]`.
```python
# Avant :
# team: Mapped["Team"] = relationship("Team", back_populates="members")

# Après :
team: Mapped["Team"] = relationship(
    "Team", back_populates="members", foreign_keys=[team_id]
)

