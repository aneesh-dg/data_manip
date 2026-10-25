import logging
from src.processor import SalaryProcessor
from src.config import load_config
from src.database import DatabaseConnection
from src.repository import EmployeeRepository


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - %(name)s - "
        "%(levelname)s - %(message)s"
    ),
)

def main():
    """Run basic database queries."""
    config = load_config()
    database = DatabaseConnection(config)
    connection = database.connect()
    try:
        repository = EmployeeRepository(connection)
        processor = SalaryProcessor(repository)
        employee_count = repository.get_employee_count()
        print(f"Total employees: {employee_count}")
        employees = repository.get_employees(limit=5)
        print("\nFirst 5 employees:")
        for employee in employees:
            print(employee)
        high_salary_count = processor.count_high_salaries(100000)
        print(
            f"\nSalary records above 100000: "
            f"{high_salary_count}"
        )
    finally:
        connection.close()
        logging.info("Database connection closed.")

if __name__ == "__main__":
    main()