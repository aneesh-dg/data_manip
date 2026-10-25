import time

import mysql.connector

from src.config import load_config
from src.repository import EmployeeRepository


def create_connection(config):
    """Create a database connection."""
    return mysql.connector.connect(
        host=config["database"]["host"],
        port=config["database"].getint("port"),
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["database"],
    )


def generator_test():
    """Process salary records using the generator."""
    config = load_config()
    connection = create_connection(config)
    repository = EmployeeRepository(connection)

    start = time.perf_counter()

    count = 0

    try:
        for row in repository.stream_salaries():
            _, salary, _, _ = row

            if salary > 100000:
                count += 1
    finally:
        connection.close()

    elapsed = time.perf_counter() - start

    print("\n--- Generator ---")
    print(f"High salary count: {count}")
    print(f"Time: {elapsed:.2f} seconds")


def fetchall_test():
    """Process salary records using fetchall."""
    config = load_config()
    connection = create_connection(config)
    cursor = connection.cursor()

    start = time.perf_counter()

    try:
        cursor.execute(
            """
            SELECT emp_no, salary, from_date, to_date
            FROM salaries
            """
        )

        rows = cursor.fetchall()

        count = 0

        for row in rows:
            _, salary, _, _ = row

            if salary > 100000:
                count += 1
    finally:
        cursor.close()
        connection.close()

    elapsed = time.perf_counter() - start

    print("\n--- Fetchall ---")
    print(f"High salary count: {count}")
    print(f"Rows fetched: {len(rows)}")
    print(f"Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    fetchall_test()