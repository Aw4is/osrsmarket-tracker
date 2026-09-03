from sqlalchemy import create_engine
from app.config.settings import get_settings
from sqlalchemy.orm import Session

# General Terms:
    # Transaction -> Group of queries, that either compelete entirely or fail completely

# ---- Engine ---- #
# Create Engine -> Engine is starting point for any SQLAlchemy Application
    # Acts as a central source of connections to a particular DB
    # Provides/Manages connection pool for these DB connections
    # DBAPI -> Python DB API Specification; talks to db. Requires:
        # Dialect -> How to talk to specific database, built around DBAPI
        # Connection Pool

# This URL/String passes important info (what db it is, how to locate db..) to engine
db_url = get_settings()
engine = create_engine(db_url)


# ---- Connection ---- #
# Connection -> Managed by Session in ORM but still nice to know:
    # Engine connects to db by providing a connection object
    # Connection object is how all interaction with the db is done 
    # Issue -> Creates an open resource against the db => want to limit our use of object
    # Fix -> Use Python context manager (with statement)
# In practice -> Context manager creates connection and executes operation in a transaction
    # ROLLBACK emitted to end the transaction (when connection is released)

# Committing Changes -> DBAPI does not automatically commit changes 
    # Uses connection.commit() to commit the transaction

# >>> with engine.connect() as conn:
# ...     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
# ...     conn.execute(
# ...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
# ...         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
# ...     )
# ...     conn.commit()

# ---- ORM & Session -----
# Fundamental transactional/database interactive object when using ORM is called the session
# Session makes use of Engine to interact with the db

with Session(engine) as session:
    