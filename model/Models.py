import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import (
    Date,
    Numeric,
    create_engine,
    Column,
    ForeignKey,
    String,
    Integer,
    CheckConstraint,
    TIMESTAMP,
    func,
    PrimaryKeyConstraint,
)

from sqlalchemy.orm import sessionmaker, declarative_base
from src.db import create_session, engine



Base = declarative_base()



class Cartorio(Base):
    __tablename__ = "cartorios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    website = Column(String(100))


class Titulo(Base):
    __tablename__ = "titulos"
    id = Column(Integer, primary_key=True)
    cartorio_id = Column(Integer, ForeignKey("cartorios.id"))
    protocolo = Column(String(255), nullable=False)
    credor = Column(String, nullable=False)
    valorprotestado = Column(Numeric(10, 2), nullable=False)
    numerotitulo = Column(String(255), nullable=False)
    dataprotesto = Column(Date, nullable=False)
    mesano = Column(Integer, nullable=False)
    CheckConstraint("mesano >= 202001 AND mesano <= 210001", name="check_mesano")
    valorboleto = Column(Numeric(10, 2), nullable=False)
    datainsert = Column(TIMESTAMP, server_default=func.now())


class Devedor(Base):
    __tablename__ = "devedores"
    titulo_id = Column(Integer, ForeignKey("titulos.id"))
    documento = Column(Numeric(14, 0), nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)


class Contato(Base):
    __tablename__ = "contatos"
    documento = Column(Numeric(14, 0), nullable=False, primary_key=True)
    telefone = Column(String(13))
    email = Column(String(100))
    PrimaryKeyConstraint("documento", "telefone")


class Zapenviado(Base):
    __tablename__ = "zapenviados"
    messageid = Column(String(100))
    titulo_id = Column(Integer, ForeignKey("titulos.id"), primary_key=True)
    whatsapp = Column(String(13))
    wa_id = Column(String(13))
    message_status = Column(String(50))
    accepted = Column(String(255))
    rejected = Column(String(255))
    response = Column(String(255))
    error = Column(String(255))
    datainsert = Column(TIMESTAMP, server_default=func.now())


Base.metadata.create_all(engine)

