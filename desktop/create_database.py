from desktop.models import Base, engine

if __name__ == "__main__":
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")