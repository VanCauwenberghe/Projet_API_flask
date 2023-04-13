from sqlalchemy import create_engine, text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    ID   SERIAL PRIMARY KEY,
    firstname    TEXT,
    lastname    TEXT,
    age     INT,
    email   CHAR(50),
    job     CHAR(50)
);
"""

create_application_table_query = """
CREATE TABLE IF NOT EXISTS application (
    ID   SERIAL PRIMARY KEY,
    appname    TEXT,
    user_name    TEXT,
    last_connexion DATE,
    user_id INT references users(ID)
);
"""

# Create
connection.execute(text(create_table_query))
connection.execute(text(create_application_table_query))

#connection.execute(text(create_table_query))
#connection.execute(text(insert_data_query))
#insert_data_query = """
#INSERT INTO film (title,director,year) VALUES ('doctor strange','scott derrickson','2016')
#"""
connection.commit()
connection.close()