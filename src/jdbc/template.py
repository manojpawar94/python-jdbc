import logging as log
from jdbc.connector import Connector

ERROR_LOG_MSG = "error '%s' occurred while executing %s query"


def create_and_execute_cursor(connection, query, parameters):
    cursor = connection.cursor()
    if not parameters:
        cursor.execute(query)
    else:
        cursor.execute(query, parameters)
    return cursor


class JdbcTemplate:

    def __init__(self, connector: Connector):
        self.database_connector = connector

    def query_for_tuple(self, query, parameters=()):
        """It executes query and returns database record as a tuple."""
        connection = None
        try:
            connection = self.database_connector.get_connection()
            cursor = create_and_execute_cursor(connection, query, parameters)
            row = cursor.fetchone()
            return row
        except self.database_connector.errors_type() as e:
            log.error(ERROR_LOG_MSG, e.msg, query, exc_info=True)
            return ()
        finally:
            self.database_connector.close_connection(connection)

    def query_for_tuple_list(self, query, parameters=()):
        """It executes query and returns database records as a list of tuples."""
        connection = None
        try:
            connection = self.database_connector.get_connection()
            cursor = create_and_execute_cursor(connection, query, parameters)
            return cursor.fetchall()
        except self.database_connector.errors_type() as e:
            log.error(ERROR_LOG_MSG, e.msg, query, exc_info=True)
            return ()
        finally:
            self.database_connector.close_connection(connection)

    def query_for_dict(self, query, parameters=()):
        """It executes query and returns database record as a dictionary."""
        connection = None
        try:
            connection = self.database_connector.get_connection()
            cursor = create_and_execute_cursor(connection, query, parameters)
            fields = [field_md[0] for field_md in cursor.description]
            return dict(zip(fields, cursor.fetchone()))
        except self.database_connector.errors_type() as e:
            log.error(ERROR_LOG_MSG, e.msg, query, exc_info=True)
            return ()
        finally:
            self.database_connector.close_connection(connection)

    def query_for_dict_list(self, query, parameters=()):
        """It executes query and returns database record as a list of dictionary."""
        connection = None
        try:
            connection = self.database_connector.get_connection()
            cursor = create_and_execute_cursor(connection, query, parameters)
            fields = [field_md[0] for field_md in cursor.description]
            return [dict(zip(fields, row)) for row in cursor.fetchall()]
        except self.database_connector.errors_type() as e:
            log.error(ERROR_LOG_MSG, e.msg, query, exc_info=True)
            return ()
        finally:
            self.database_connector.close_connection(connection)

    def update(self, query, parameters=()):
        """It executes insert, update queries."""
        connection = None
        try:
            connection = self.database_connector.get_connection()
            cursor = create_and_execute_cursor(connection, query, parameters)
            connection.commit()
            return cursor.lastrowid
        except self.database_connector.errors_type() as e:
            log.error(ERROR_LOG_MSG, e.msg, query, exc_info=True)
            return -1
        finally:
            self.database_connector.close_connection(connection)
