from sqlalchemy.future import select
from sqlalchemy import update
from . import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TYPE_CHECKING, List, Optional

# if TYPE_CHECKING:
#     from . import schemas

async def get_employee(db: AsyncSession, emp_id: int) -> Optional[models.Employee]:
    q = await db.execute(select(models.Employee).where(models.Employee.id == emp_id))
    return q.scalars().first()


async def list_employees(db: AsyncSession, limit: int = 100, offset: int = 0) -> List[models.Employee]:
    q = await db.execute(select(models.Employee).limit(limit).offset(offset))
    return q.scalars().all()


async def create_employee(db: AsyncSession, emp_in: schemas.EmployeeCreate) -> models.Employee:
    emp = models.Employee(**emp_in.dict())
    db.add(emp)
    await db.commit()
    await db.refresh(emp)
    return emp


async def update_employee_status(db: AsyncSession, emp_id: int, status: str):
    await db.execute(update(models.Employee).where(models.Employee.id == emp_id).values(status=status))
    await db.commit()