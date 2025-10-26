from sqlmodel import create_engine, SQLModel
from back.src import models
class DBEngine:
    db_connection_string: str
    def __init__(self):
        self.db_connection_string = f"postgresql://admin:admin@localhost/herokoou_db"
        self.engine=create_engine(self.db_connection_string, echo=True)
        
    
    def init(self):
        SQLModel.metadata.create_all(self.engine)
    
    def get_metadata(self):
        return SQLModel.metadata