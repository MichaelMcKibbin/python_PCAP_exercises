sales_map=[
    {"country": "Spain", "sales": 1000},
    {"country": "France", "sales": 2000},
    {"country": "Germany", "sales": 3000},
    {"country": "Italy", "sales": 4000},
    {"country": "Ireland", "sales": 5000}
]

countries = map(lambda x: x["country"], sales_map)
print(list(countries))

sales = map(lambda x: x["sales"], sales_map)
print(list(sales))
