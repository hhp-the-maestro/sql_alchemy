from insert_data import engine, cookies
from sqlalchemy import update, delete, select

# Updating the cookies table using the update method

u = update(cookies).where(cookies.c.cookie_name == 'choco_chip')
u = u.values(quantity=(cookies.c.quantity + 120))
result = engine.connect().execute(u)
print(result.rowcount)

s = select([cookies]).where(cookies.c.cookie_name == 'choco_chip')
result = engine.connect().execute(s).first()
for key in result.keys():
    print(key, result[key])

# deleting a row using the delete method
d = delete(cookies).where(cookies.c.cookie_name == 'choco_chip')
result = engine.connect().execute(d)
print(result.rowcount)

s = select([cookies]).where(cookies.c.cookie_name == 'choco_chip')
result = engine.connect().execute(s).fetchall()
print(len(result))