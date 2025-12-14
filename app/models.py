from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum


Base = declarative_base()


class StatusEnum(str, enum.Enum):
    active = "active"
    inactive = "inactive"


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department_name = Column(String(128), nullable=False, unique=True)
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    phonenumber = Column(String(32), nullable=True)
    doj = Column(Date, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.active)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    department = relationship("Department", back_populates="employees")