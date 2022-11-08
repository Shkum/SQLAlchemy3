import sqlalchemy as db

# constant - DB name
DATABASE_NAME = 'sqlite.db'

# create engine (driver) for used DB
engine = db.create_engine(f'sqlite:///{DATABASE_NAME}')

# connecting of engine to DB
connection = engine.connect()

# create variable for DB
metadata = db.MetaData()

# create new Table at DB (virtual, in memory, not in the DB file)
products = db.Table('Products', metadata,
                    db.Column('product_id', db.Integer, primary_key=True),
                    db.Column('product_name', db.Text),
                    db.Column('supplier_name', db.Text),
                    db.Column('price_per_tonne', db.Integer)
                    )

# create DB and Table products in it IN FILE
metadata.create_all(engine)
# ________________ DATABASE AND TABLE INSIDE CREATED________________

# creating virtual data for Table
insertion_query = products.insert().values([
    {'product_name': 'Banana', 'supplier_name': 'United_Bananas', 'price_per_tonne': 7000},
    {'product_name': 'Avocado', 'supplier_name': 'United_Avocados', 'price_per_tonne': 12000},
    {'product_name': 'Tomatoes', 'supplier_name': 'United_Tomatoes', 'price_per_tonne': 3100}

])

# ______________ADD DATA TO DB _____________________
# add data to virtual Table (in memory)
# connection.execute(insertion_query)


# ____________ GET DATA FROM DB _______________
# create query to get data from Table products :
select_all_query = db.select([products])

# execute query above
select_all_result = connection.execute(select_all_query)

# print all data from Tablr products
print(select_all_result.fetchall())

# get only data with price 12000
select_price_query = db.select([products]).where(products.columns.price_per_tonne==12000)
# execute query above
select_price_result = connection.execute(select_price_query)
result = select_price_result.fetchall()
print(result)
print(result[0]['product_name'])

# _______________ UPDATE DATA IN DB ____________________


