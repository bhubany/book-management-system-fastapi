from sqlmodel import SQLModel, create_engine

engine = create_engine("postgresql://pg-admin:password123@localhost:5432/bms")

def create_tables():
    SQLModel.metadata.create_all(engine)
