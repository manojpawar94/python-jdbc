# Python JDBC

It is jdbc utility helps to query on the RDBMS databases. It avoids the boilerplate code required while executing the
sql query. It supports database connection pool as well.

## Examples

```python
from jdbc.mysql_connector import MySQLConnector
from jdbc.template import JdbcTemplate

config = {
    "host": "localhost",
    "port": 3306,
    "database": "xxx",
    "user": "root",
    "password": ""
}

# initialize MySQLConnector and JdbcTemplate once in program (in __init__.py)
mysql_conn = MySQLConnector(config)
jdbcTemplate = JdbcTemplate(mysql_conn)

# query to retrieve tuple
jdbcTemplate.query_for_tuple("select * from users where user_id = ? ", 1234)

# query to retrieve list of tuples
jdbcTemplate.query_for_tuple_list("select * from users where is_active = ?", 'A')

# query to retrieve dictionary 
jdbcTemplate.query_for_dict("select * from users where user_id = ? ", 1234)

# query to retrieve list of dictionary
jdbcTemplate.query_for_dict_list("select * from users where is_active = ?", 'A')

# query to insert record
jdbcTemplate.update("Insert into users (first_nam, last_nam) values (?, ?)", "Manoj", "Pawar")

# query to update record
jdbcTemplate.update("Update users set is_activev = ? where user_id = ?", 'A', 1234)
```