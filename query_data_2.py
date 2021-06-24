import insert_data
from insert_data import engine, cookies
from sqlalchemy import select, cast, Numeric, and_, or_, not_, String
from sqlalchemy.sql import func

# sum up values of a column using func.sum method
s = select([func.sum(cookies.c.unit_cost)])
rp = engine.connect().execute(s)
print(f'{rp.keys()}\n{rp.scalar()}')

# count the number of items using func.count
s = select([func.count(cookies.c.cookie_name)])
rp = engine.connect().execute(s)
print(f'{rp.keys()}\n{rp.scalar()}')

#  set label for a query by which we can access it
s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
rp = engine.connect().execute(s)
result = rp.first()
print(result.keys())
print(result.inventory_count)

# using filter with 'where' statement to search for a particular value in a column
s = select([cookies]).where(cookies.c.quantity == 12)
rp = engine.connect().execute(s)
result = rp.first()
print(result._mapping.items())
# print(rp.fetchall())

# using the cast method to convert the type of the value retrieved from the database
s = select([cookies.c.cookie_name, cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)).label('inv_cost')])
rp = engine.connect().execute(s)
for row in rp:
    print(f'{row.cookie_name} - {row.inv_cost}')

# we can use conjunctions to retrieve data for a desired output
# we can chain multiple where clause together but using conjunctions would provide more readability

s = select([cookies]).where(
    and_(
        cookies.c.quantity > 10,
        cookies.c.unit_cost > 0.40
    )
)

for row in engine.connect().execute(s):
    print(row)

print('\n')
s = select([cookies]).where(
    or_(
        cookies.c.cookie_name.contains('chip'),
        cookies.c.quantity.between(5, 15)
    ),
    not_(
        cookies.c.cookie_name.contains('caramel')
    )
)

for row in engine.connect().execute(s):
    print(row)
