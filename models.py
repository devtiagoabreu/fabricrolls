# models.py
from sqlalchemy import create_engine, Column, String, Numeric, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tecido(Base):
    __tablename__ = 'tecidos'
    id = Column(Integer, primary_key=True)
    ordem = Column(String(6), nullable=False)
    lote = Column(String(6), nullable=False)
    produto = Column(String(6), nullable=False)
    situacao = Column(String(3), nullable=False)
    cor = Column(String(5), nullable=False)
    desenho = Column(String(5), nullable=False)
    variante = Column(String(5), nullable=False)
    categoria = Column(String(2), nullable=False)
    numero_rolo = Column(String(10), nullable=False)  # Zero-filled (ex: "0000001234")
    metros = Column(Numeric(18, 5), nullable=False)
    peso_liquido = Column(Numeric(18, 5), nullable=False)
    peso_bruto = Column(Numeric(18, 5), nullable=False)
    largura = Column(Numeric(18, 5), nullable=False)