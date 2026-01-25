from datetime import date
from sqlmodel import SQLModel, Field

class BudgetModel(SQLModel, table=True):
    __tablename__ = "budget"
    id: str | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    name: str | None = Field()
    start_date: date | None = Field(default=None)
    end_date: date | None = Field(default=None)
    active: bool | None = Field(default=True)
    # parent: bool | None = Field(default=False)
