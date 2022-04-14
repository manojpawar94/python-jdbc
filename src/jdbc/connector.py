class Connector:
    def get_connection(self):
        """It is abstract method. The implementing class must return the connection object."""
        pass

    def errors_type(self):
        """It is an abstract method. The implementing class must return the class extending Exception"""
        pass

    def close_connection(self, connection):
        """It closes the database connection."""
        pass
