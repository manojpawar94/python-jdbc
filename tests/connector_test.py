import unittest
from jdbc.mysql_connector import MySQLConnector


class ConnectorTest(unittest.TestCase):
    __dbConfig = {
        "host": "localhost",
        "port": 3306,
        "database": "xxx",
        "user": "root",
        "password": ""
    }

    def test_MySQLConnector(self):
        mysql_conn = MySQLConnector(self.__dbConfig)
        self.assertIsNotNone(mysql_conn, "MySQL connection object must be initialized")  # add assertion here


if __name__ == '__main__':
    unittest.main()
