from sqlalchemy import select, update
from insert_data import cookies
from insert_data_2 import users, orders, list_items, engine


def ship_it(order_id):
    s = select([list_items.c.cookie_id, list_items.c.quantity])
    s = s.where(list_items.c.order_id == order_id)
    cookies_to_ship = engine.connect().execute(s)

    for cookie in cookies_to_ship:
        s = select([cookies.c.quantity]).where(cookies.c.cookie_id == cookie.cookie_id)
        rp = engine.connect().execute(s)
        rp = rp.first()
        if rp.quantity >= cookie.quantity:
            u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
            u = u.values(quantity=cookies.c.quantity - cookie.quantity)
            result = engine.connect().execute(s)

            u = update(orders).where(orders.c.order_id == order_id)
            u = u.values(shipped=True)
            result = engine.connect().execute(u)

ship_it(2)

s = select([orders])
r = engine.connect().execute(s)
r = r.fetchall()

print(r)