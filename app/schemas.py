from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class DepartmentBase(BaseModel):
    department_id: Optional[int]
    department_name: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentOut(DepartmentBase):
    department_id: int
    model_config = {"from_attributes": True}
    # class Config:
    #     orm_mode = True


class EmployeeBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phonenumber: Optional[str]
    doj: Optional[date]
    status: Optional[str] = "active"
    department_id: Optional[int]


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int
    model_config = {"from_attributes": True}
    # class Config:
    #     orm_mode = True