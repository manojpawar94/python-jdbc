from src.jdbc.connector import Connector
from mysql.connector.pooling import MySQLConnectionPool, PooledMySQLConnection
from mysql.connector.errors import Error


class MySQLConnector(Connector):

    def __init__(self, config, pool_name="default_pool", pool_size=10):
        self.__connPool = MySQLConnectionPool(pool_name=pool_name,
                                              **config,
                                              pool_size=pool_size)

    def get_connection(self) -> PooledMySQLConnection:
        """It returns the PooledMySQLConnection object"""
        return self.__connPool.get_connection()

    def errors_type(self):
        """It returns the mysql.connector.errors.Error"""
        return Error

    def close_connection(self, connection: PooledMySQLConnection):
        """It closes the PooledMySQLConnection"""
        if connection is not None:
            connection.close()
