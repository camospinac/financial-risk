from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_transaction(db: AsyncSession, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction

async def get_transaction(db: AsyncSession, transaction_id: int):
    result = await db.execute(select(models.Transaction).where(models.Transaction.id == transaction_id))
    return result.scalar_one_or_none()

async def get_transactions_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.Transaction).where(models.Transaction.user_id == user_id))
    return result.scalars().all()