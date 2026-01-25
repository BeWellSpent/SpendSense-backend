from sqlmodel import select, Session
from db.model.budget import BudgetModel
from models.budget import Budget
from uuid import uuid4
import logging as log

class BudgetRepository:
    def __init__(self):
        self._model = BudgetModel

    def get_budget_by_user_id(self, user_id: int, session: Session):
        statement = select(self._model).where(self._model.user_id == user_id)
        result = session.exec(statement).all()
        return result
    
    def create_budget(self, session: Session, budget_data: Budget):
        budgets = self.get_budget_by_user_id(budget_data.user_id, session)
        for budget in budgets:
            if budget and budget.name == budget_data.name:
                log.error("[BudgetRepository.create_budget] Budget with name %s already exists for user %s", budget_data.name, budget_data.user_id)
                raise Exception(f"Budget with name {budget_data.name} already exists for user {budget_data.user_id}")
        
        log.info("[BudgetRepository.create_budget] Existing budgets for user %s: %s", budget_data.user_id, budgets)
        new_budget = BudgetModel()
        new_budget.id = str(uuid4())
        new_budget.name = budget_data.name
        new_budget.user_id = budget_data.user_id
        # new_budget.start_date = budget_data.start_date
        # new_budget.end_date = budget_data.end_date
        new_budget.active = True
        # new_budget.parent = True
        try:
            session.add(new_budget)
            session.commit()
        except Exception as e:
            log.error("[BudgetRepository.create_budget] Error creating budget: %s", e)
            log.exception(e)
            session.rollback()
            return None
            
        return new_budget
        
    def add_people_to_budget(self, session: Session, budget_id: str, people: list[dict]):
        budget = session.get(self._model, budget_id)
        if not budget:
            raise ValueError("Budget not found")
        # Assuming budget has a 'people' attribute which is a list
        if not hasattr(budget, 'people'):
            budget.people = []

        for person in people:
            if person in budget.people:
                raise Exception(f"Person {person} already in budget, cannot add again.")
            
        budget.people.extend(people)
        session.add(budget)
        session.commit()
        return budget