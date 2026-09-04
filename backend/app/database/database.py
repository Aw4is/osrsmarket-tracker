from sqlalchemy import create_engine
from app.config.settings import get_settings
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session

# General Terms:
    # Transaction -> Group of queries, that either compelete entirely or fail completely
    # Typical DB Connection:
        # App uses database driver to open a connectiion
        # network socket is opened to connect to app and db
        # user is authenticated, opertion completes and connection may be closed
        # network socket is closed
    # Pooling DB connections:
        # Why -> As app scales up, constant opening and closing of connection
            # becomes more expensive and impact app performance
        # Sol -> Find a way to keep connections open and pass them when needed
        # What -> Reduce cost of opening and closing connections by maintaining
            # pool of connections 
        # Do not always help -> Expensive to open/close/maintain these connections

# ---- Engine ---- #
# Create Engine -> Engine is starting point for any SQLAlchemy Application
    # Acts as a central source of connections to a particular DB
    # Provides/Manages connection pool for these DB connections
    # DBAPI -> Python DB API Specification; talks to db. Requires:
        # Dialect -> How to talk to specific database, built around DBAPI
        # Connection Pool

# This URL/String passes important info (what db it is, how to locate db..) to engine
    # returns setting objects, we need to access DB url
db_url = get_settings()
engine = create_engine(db_url.DATABASE_URL)

# All our entites (item, snapshot etc) share the same SQLAlchemy metadata
class Base(DeclarativeBase):
    pass

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
# Session -> Estabilishes all conversations with the db and represents holding zone
 # for all objects which are loaded/associated with it during its span
 # Provides interface where queries can be made that will return/moidfy ORM mapped obj
# ORM objects are maintained inside Session inside identity map
    # Data structure that maintains unique copies of each object by primary id 
# Session -> once queries issued, requests connection from an Engine
    # and then estabilishes a transaction on that connection
    # transaction remains in effect until Session is instructed to commit/rollback
    # when transaction ends, connection resource is released to connection pool
# Uses unit of work pattern:
    # When DB is about to be queried/transaction committed (making db change perm)
    # Session first flushes all pending changes stored in memory to the database


# Create a Session factory -> Can call later whenever a request needs one 
SessionLocal = sessionmaker(bind=engine)

# ---- Dependency ---- #
# Uses DI to provide DB session for endpoint (like Get /items)

# A FastAPI dependency is a function that returns a value
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



