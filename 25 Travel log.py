travel_log = [
    {
        "Country": "France",
        "Visits": 12,
        "cities":["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "Visits": 5,
        "cities":["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    next_item = {}
    next_item["Country"] = country
    next_item["Visits"] = visits
    next_item["cities"] = cities
    travel_log.append(next_item)

add_new_country("Russia", 2, ["Moscow", "Saint Peteraburg"])
print(travel_log)