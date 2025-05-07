# auth.py
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()  # Salvar em variável de ambiente na produção

def encrypt_password(password: str) -> bytes:
    return Fernet(KEY).encrypt(password.encode())

def decrypt_password(encrypted: bytes) -> str:
    return Fernet(KEY).decrypt(encrypted).decode()