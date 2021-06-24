from sqlalchemy import select
from sqlalchemy.sql import func
from insert_data_2 import orders, users, list_items, engine
from insert_data import cookies
import insert_data, insert_data_2

columns = [orders.c.order_id, users.c.username, users.c.phone,
           cookies.c.cookie_name, list_items.c.quantity, list_items.c.extended_cost]

# we can query the related data using join

cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(list_items).join(users).join(cookies)).where(
    users.c.username == 'cookiemon'
)
result = engine.connect().execute(cookiemon_orders).fetchall()

print(cookiemon_orders, '\n')

for row in result:
    print(row)

# using outerjoins to select multiple tables

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = engine.connect().execute(all_orders).fetchall()

for row in result:
    print(row)

# conditional chaining


def get_orders_by_customer(cust_name, shipped=None, details=False):
    columns = [orders.c.order_id, users.c.username, users.c.phone]
    joins = users.join(orders)
    if details:
        columns.extend([cookies.c.cookie_name, list_items.c.quantity, list_items.c.extended_cost])
        joins = joins.join(list_items).join(cookies)

    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username==cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped==shipped)
    result = engine.connect().execute(cust_orders).fetchall()
    return result

print(get_orders_by_customer('coolie', details=True, shipped=True))