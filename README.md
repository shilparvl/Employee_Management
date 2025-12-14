# Employee_Management

#Run below command to connect database and check tables 
docker exec -it postgres psql -U postgres -d employee_management

\dt - to list tables

insert into departments (id, department_name) values(1, 'engineering');

Commands to run Employee_Management app
docker-compose down -v
docker-compose build 
docker-compose up

#Optional
docker build -t employee-api .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000