from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal
from . import crud, schemas
from .services import validate_user  # <-- Nueva línea

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/transactions", response_model=schemas.TransactionOut)
async def create(transaction: schemas.TransactionCreate, db: AsyncSession = Depends(get_db)):
    is_valid_user = await validate_user(transaction.user_id)
    if not is_valid_user:
        raise HTTPException(status_code=400, detail="User not found")

    return await crud.create_transaction(db, transaction)

@router.get("/transactions/{transaction_id}", response_model=schemas.TransactionOut)
async def get(transaction_id: int, db: AsyncSession = Depends(get_db)):
    transaction = await crud.get_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions", response_model=list[schemas.TransactionOut])
async def list_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_transactions_by_user(db, user_id)
