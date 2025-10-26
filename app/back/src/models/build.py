from sqlmodel import Field, SQLModel
class Build(SQLModel, table=True):
    id:int = Field(primary_key=True)

    def __init__(self, id):
        self.id = id
