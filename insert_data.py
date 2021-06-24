from sqlalchemy import insert
# importing the previously created empty database here to which we will feed some data
from create_table import cookies, engine, orders, users, list_items

# we can insert the values of a single row using the 'insert' method
ins1 = cookies.insert().values(
    cookie_name='choco_chip',
    cookie_recipe_url="http://some.awesome.me/cookie/recipe.html",
    cookie_sku='cc01',
    quantity='12',
    unit_cost='0.50'
)

# print(str(ins1))
# print(ins1.compile().params)


ins2 = insert(cookies).values(
    cookie_name='caramel_craft',
    cookie_recipe_url='https://some.aweso.me/cookie/recipe.html',
    cookie_sku='Ca02',
    quantity='12',
    unit_cost='0.75'
)

i = [ins1, ins2]
for j in i:
    with engine.connect() as connection:
        result = connection.execute(j)
    # print(result.inserted_primary_key)

ins3 = cookies.insert()

# we can also insert values using the connection.execute with the first argument as the insert and then values

result = engine.connect().execute(
    ins3,
    cookie_name='dark_choco_chip',
    cookie_recipe='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='cc03',
    quantity='15',
    unit_cost='0.70'
)
# print(result.inserted_primary_key)
# we can insert multiple rows in a table using a list of dictionaries
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
        'cookie_sku': 'pb01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
        'cookie_sku': 'pb02',
        'quantity': '24',
        'unit_cost': '0.35'
    }
]

ins4 = cookies.insert()
new_result = engine.connect().execute(ins4, inventory_list)

