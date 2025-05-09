from auth import get_password_hash
from database import SessionLocal
from models import User

db = SessionLocal()

# Cria usuário admin se não existir
if not db.query(User).filter(User.username == "admin").first():
    db_user = User(
        username="admin",
        hashed_password=get_password_hash("admin123"),
        is_active=True
    )
    db.add(db_user)
    db.commit()
    print("✅ Usuário admin criado: usuario=admin | senha=admin123")
else:
    print("⚠️ Usuário admin já existe")

db.close()