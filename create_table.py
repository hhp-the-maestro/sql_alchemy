from datetime import datetime
from sqlalchemy import (MetaData, Table, create_engine, ForeignKey, Column,
                        Integer, Numeric, String, DateTime, Boolean)

# the metadata is the bonding element which ties Table together

metadata = MetaData()

# Creating multiple tables in our database using the 'Table' method

cookies = Table(
    'cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', String(13))
)


users = Table(
    'users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('customer_number', Integer(), autoincrement=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now()),
    Column('update_on', DateTime(), default=datetime.now(), onupdate=datetime.now())
)

orders = Table(
    'orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)
)

# The ForeignKey is used like an import statement in python which is used to get the column from other tables

list_items = Table(
    'line_items', metadata,
    Column('list_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', String())
)

# Creating the instance of the database using sqlalchemy.create_engine
engine = create_engine("sqlite:///:memory:")
# we tie up the columns of the table using the metadata and create the database
metadata.create_all(engine)