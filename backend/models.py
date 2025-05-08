from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

class Tecido(Base):
    __tablename__ = "tecidos"
    id = Column(Integer, primary_key=True)
    ordem = Column(String(6), nullable=False)
    lote = Column(String(6), nullable=False)
    produto = Column(String(6), nullable=False)
    situacao = Column(String(3), nullable=False)
    cor = Column(String(5), nullable=False)
    desenho = Column(String(5), nullable=False)
    variante = Column(String(5), nullable=False)
    categoria = Column(String(2), nullable=False)
    numero_rolo = Column(String(10), nullable=False)  # Ex: "0000001234"
    metros = Column(Numeric(18, 5), nullable=False)
    peso_liquido = Column(Numeric(18, 5), nullable=False)
    peso_bruto = Column(Numeric(18, 5), nullable=False)
    largura = Column(Numeric(18, 5), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

