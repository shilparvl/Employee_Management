from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import crud, schemas, deps, cache


router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/{emp_id}", response_model=schemas.EmployeeOut)
async def read_employee(emp_id: int, db: AsyncSession = Depends(deps.get_db)):
    # try cache first
    cached = await cache.get_employee_cache(emp_id)
    if cached:
        return cached
    emp = await crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    # out = schemas.EmployeeOut.from_orm(emp)
    # # cache
    # await cache.set_employee_cache(emp_id, out.dict())
    # return out

    out = schemas.EmployeeOut.model_validate(emp)
    await cache.set_employee_cache(emp_id, out.model_dump())
    return out


@router.post("/", response_model=schemas.EmployeeOut)
async def create_employee(emp_in: schemas.EmployeeCreate, db: AsyncSession = Depends(deps.get_db)):
    emp = await crud.create_employee(db, emp_in)
    return schemas.EmployeeOut.model_validate(emp)
