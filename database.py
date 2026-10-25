import logging

import mysql.connector
from mysql.connector import Error


logger = logging.getLogger(__name__)


class DatabaseConnection:
    """Manage connections to the MySQL database."""

    def __init__(self, config):
        self.config = config

    def connect(self):
        """Create and return a MySQL connection."""
        try:
            connection = mysql.connector.connect(
                host=self.config["database"]["host"],
                port=self.config["database"].getint("port"),
                user=self.config["database"]["user"],
                password=self.config["database"]["password"],
                database=self.config["database"]["database"],
            )

            logger.info("Successfully connected to MySQL.")
            return connection

        except Error:
            logger.exception("Failed to connect to MySQL.")
            raise