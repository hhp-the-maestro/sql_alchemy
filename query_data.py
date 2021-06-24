from sqlalchemy.sql import select
from sqlalchemy import desc
from sqlalchemy.sql import func
# importing the previously created file which inserts data to the database
from insert_data import cookies, engine

# we can get the values of the table using the select method which is same as SQL's SELECT

s = select([cookies])
rp = engine.connect().execute(s)

# querying all the values of the db using the fetchall

result = rp.fetchall()
print(str(s))
print(result)

# different approaches for querying particular row value from the db

first_row = result[0]
print(first_row[1])
print(first_row.quantity)
print(first_row[cookies.c.unit_cost])
print('\n')

rp = engine.connect().execute(s)
for record in rp:
    print(record.cookie_name)
print('\n')

# Querying a particular value from the db

s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = engine.connect().execute(s)
print(rp.keys())
result = rp.first()
print(result)
print('\n')

# we can get queries in the order by using 'order_by' method
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
rp = engine.connect().execute(s)
for cookie in rp:
    print(f'{cookie.cookie_name}: {cookie.quantity}')

print('\n')

# we can also get the order in descending using the 'desc' method
s = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(desc(cookies.c.quantity))
rp = engine.connect().execute(s)
for cookie in rp:
    print(f'{cookie.cookie_name}: {cookie.quantity}')

# we can limit the number of cookies returned using the 'limit' method

s = select([cookies.c.cookie_name]).order_by(cookies.c.quantity).limit(2)
rp = engine.connect().execute(s)
print([result.cookie_name for result in rp])

