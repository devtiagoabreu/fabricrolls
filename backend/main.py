from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import (
    create_access_token,
    authenticate_user,
    get_current_user,
    get_db,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from datetime import timedelta
from sqlalchemy.orm import Session

app = FastAPI()

# Rota de login completa
@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Rota protegida de exemplo
@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user