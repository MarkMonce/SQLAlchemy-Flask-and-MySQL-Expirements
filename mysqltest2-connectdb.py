from sqlalchemy import create_engine, Table, MetaData

# Specify the MySQL connection string
# mysql+pymysql://<username>:<password>@<host>/<dbname>
DATABASE_URI = 'mysql+pymysql://root:Naples727575!!@127.0.0.1/payroll'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI, echo=True)

# Metadata object to hold info about tables
metadata = MetaData()

# Reflect an existing database into a new model
metadata.reflect(bind=engine)

# Assuming we have a table named 'example_table' in the databasecl
example_table = metadata.tables['employees']

# Connect to the database
with engine.connect() as connection:
    # Execute a query to fetch all records from 'example_table'
    result = connection.execute(example_table.select())

    # Print the results
    for row in result:
        print(row)


# Close the engine (optional, as it's automatically managed)
engine.dispose()