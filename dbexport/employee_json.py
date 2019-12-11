from dbexport.config import get_session
from dbexport.models import Employee
from sqlalchemy.sql import func
import json 

db_url="postgres://mikhail:d89NN9yS@35.178.210.138:80/sample"

#csv_file = open("employees.csv", mode="w")
#fields = ["id", "first_name", "last_name", "email", "gender", "favorite_color"]
#fields = ["id", "first_name", "last_name"]
#csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
#csv_writer.writeheader()

session = get_session(db_url)

employees = []

for employee in session.query(Employee).limit(10).all():
    employees.append({
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name
    })


with open("employee.json","w") as f:
    json.dump(employees,f)
