from fastapi import APIRouter, Depends, Body
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
from sqlmodel import Session
from db.session import get_session
from service.budget_service import BudgetService
from schemas.budget import BudgetCreateRequest, BudgetCreateResponse
import logging as log

router = APIRouter()

@router.put("/budget/create")
async def create_budget(budget_data: Annotated[BudgetCreateRequest, Body(embed=True)], session: Session = Depends(get_session)):
    log.info("[create_budget] Creating budget with data: %s", budget_data)
    try:
        budget = BudgetService().create_budget(session, budget_data)
        if budget is None:
            raise HTTPException(status_code=500, detail="Failed to create budget")
        log.info("[create_budget] Budget created successfully: %s", budget)        
        response = BudgetCreateResponse(
            id=budget.id,
            user_id=budget.user_id,
            name=budget.name,
            start_date=str(budget.start_date) if hasattr(budget, 'start_date') and budget.start_date else None,
            end_date=str(budget.end_date) if hasattr(budget, 'end_date') and budget.end_date else None,
            active=budget.active
        )
        return JSONResponse(status_code=201, content={"success": True, "budget": response.model_dump()})
    except Exception as e:
        log.error("[create_budget] Error creating budget: %s", e)
        log.exception(e)
        return JSONResponse(status_code=400, content={"success": False, "error": str(e)})
    
@router.put("/budget/{budget_id}")
async def add_people(budget_id: str, session: Session = Depends(get_session)):
    return BudgetService().get_budget(session, budget_id)
