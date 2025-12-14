from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import schemas, deps, crud  # adjust imports based on your project structure

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

# Get all departments
@router.get("/", response_model=List[schemas.DepartmentOut])
async def read_departments(db: AsyncSession = Depends(deps.get_db)):
    departments = await crud.get_departments(db)
    return departments

# Get a single department by id
@router.get("/{department_id}", response_model=schemas.DepartmentOut)
async def read_department(department_id: int, db: AsyncSession = Depends(deps.get_db)):
    department = await crud.get_department(db, department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

# Create a new department
@router.post("/", response_model=schemas.DepartmentOut)
async def create_department(department_in: schemas.DepartmentCreate, db: AsyncSession = Depends(deps.get_db)):
    department = await crud.create_department(db, department_in)
    return department
