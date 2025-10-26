from sqlmodel import Field, SQLModel
class Build(SQLModel, table=True):
    __tablename__="builds"
    id:int = Field(primary_key=True)
    external_id:str 

    def __init__(self, id):
        self.id = id
