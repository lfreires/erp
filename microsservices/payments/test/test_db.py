# test_db.py
"""
Script de teste para criar o database/schema e verificar as tabelas.
"""
from infrastructure.database import init_db, get_engine
from models import Base


def main():
    # 1) Inicializa o database: cria schema + tabelas
    init_db()
    print("Banco e tabelas criados/comprovados com sucesso.")

    # 2) Conecta usando engine e lista as tabelas existentes
    engine = get_engine()
    with engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
    
    print("Tabelas no database:")
    for table in tables:
        print(f" - {table}")


if __name__ == '__main__':
    main()
