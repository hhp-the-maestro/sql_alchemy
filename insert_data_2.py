from sqlalchemy import insert
from insert_data import engine, users, orders, list_items

customer_list = [
    {
        'username': 'coolie',
        'email': 'coolie@cookie.com',
        'phone': '111-111-1111',
        'password': 'password'
    },
    {
        'username': 'cookiemon',
        'email': 'mone@cookie.com',
        'phone': '111-112-1111',
        'password': 'password'
    },
    {
        'username': 'cookiecon',
        'email': 'cone@cookie.com',
        'phone': '112-112-1111',
        'password': 'password'
    },
    {
        'username': 'rangerB',
        'email': 'rbe@cookie.com',
        'phone': '311-112-1111',
        'password': 'password'
    },
    {
        'username': 'kelly',
        'email': 'kelly@cookie.com',
        'phone': '111-112-1234',
        'password': 'password'
    }
]

ins = users.insert()
engine.connect().execute(ins, customer_list)

ins2 = orders.insert()
ordering = [
    {
        'order_id': 1,
        'user_id': 1
    },
    {
        'order_id': 2,
        'user_id': 2
    },
    {
        'order_id': 3,
        'user_id': 1
    },
    {
        'order_id': 4,
        'user_id': 3
    },
    {
        'order_id': 5,
        'user_id': 4
    }
]

result = engine.connect().execute(ins2, ordering)

ins3 = list_items.insert()

order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': None,
        'extended_cost': 1.00
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 3,
        'extended_cost': 5.00
    },
    {
        'order_id': 3,
        'cookie_id': 2,
        'quantity': 5,
        'extended_cost': 3.00
    },
    {
        'order_id': 4,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 2.50
    },
    {
        'order_id': 5,
        'cookie_id': 1,
        'quantity': 13,
        'extended_cost': 3.07
    }
]

engine.connect().execute(ins3, order_items)