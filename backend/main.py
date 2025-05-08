from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
from models import User, Tecido
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models

app = FastAPI()

# Cria as tabelas
models.Base.metadata.create_all(bind=engine)

# Rotas
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    return {
        "access_token": create_access_token({"sub": user.username}),
        "token_type": "bearer"
    }

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user