from sqlalchemy import create_engine, text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_table_query = """

"""

# Create
connection.execute(text(create_table_query))
#connection.execute(text(create_table_query))
#connection.execute(text(insert_data_query))
insert_data_query = """

"""
connection.commit()
connection.close()



