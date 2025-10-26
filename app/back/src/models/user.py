from sqlmodel import Field, SQLModel
class User(SQLModel, table=True):
    
    id:int = Field(primary_key=True)
    external_id: str
    email: str = Field()

    def __init__(self, id):
        self.id = id