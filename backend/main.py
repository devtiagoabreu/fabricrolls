from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Tecido

app = FastAPI()
engine = create_engine("sqlite:///tecidos.db")
Session = sessionmaker(bind=engine)

# Rotas da API (exemplo)
@app.get("/tecidos")
def listar_tecidos():
    db = Session()
    tecidos = db.query(Tecido).all()
    return tecidos