from pydantic import BaseModel, Field
from pydantic import BaseModel, Field
from models.budget import Income, Expense, Person

class BaseBudgetEditRequest(BaseModel):
    budget_id: str | None = Field(default=None, title="budget identifier")

class BudgetCreateRequest(BaseModel):
    user_id : int | None = Field(default=None, title="user identifier")
    name : str | None = Field(default=None, title="budget name")

class BudgetCreateResponse(BaseModel):
    id: str | None = None
    user_id: int | None = None
    name: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    active: bool | None = None

class AddPeopleToBudgetRequest(BaseBudgetEditRequest):
    people: list[Person] | None = Field(default=None, title="people involved in the budget")

class AddIncomeToBudgetRequest(BaseBudgetEditRequest):
    income: list[Income] | None = Field(default=None, title="income details")
    
class AddExpenseToBudgetRequest(BaseBudgetEditRequest):
    expense: list[Expense] | None = Field(default=None, title="expense details")
