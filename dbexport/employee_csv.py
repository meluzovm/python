from dbexport.config import get_session
from dbexport.models import Employee
from sqlalchemy.sql import func
import csv

db_url="postgres://mikhail:d89NN9yS@35.178.210.138:80/sample"

csv_file = open("employees.csv", mode="w")
#fields = ["id", "first_name", "last_name", "email", "gender", "favorite_color"]
fields = ["id", "first_name", "last_name"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
csv_writer.writeheader()

session = get_session(db_url)

for employee in session.query(Employee).limit(10).all():
    csv_writer.writerow(
        {
            "id": employee.id,
            "first_name": employee.first_name,
            "last_name": employee.last_name
        }
    )

"""
SQL: select product_id,count(*) as review_count,avg(rating) as avg_rating from Review group by product_id;
Python:
reviews_statement = (
    session.query(
        Review.product_id,
        func.count("*").label("review_count"),
        func.avg(Review.rating).label("avg_rating"),
    )
    .group_by(Review.product_id)
    .subquery()
)

"""


csv_file.close()
