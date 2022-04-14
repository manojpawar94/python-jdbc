import unittest
from src.jdbc.mysql_connector import MySQLConnector


class DatabaseConnectorTest(unittest.TestCase):
    __dbConfig = {
        "host": "localhost",
        "port": 3306,
        "database": "xxx",
        "user": "root",
        "password": ""
    }

    def test_something(self):
        mysql_conn = MySQLConnector(self.__dbConfig)
        self.assertIsNotNone(mysql_conn, "MySQL connection object must be initialized")  # add assertion here


if __name__ == '__main__':
    unittest.main()
