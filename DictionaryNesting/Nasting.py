capitals={"France":"Paris",
          "Germany":"Berlin"}

travel_log=[
    {'country':"France",
     "cities":["Paris","Lille","Dijon"],
     "total":12},
    {'country':"Germany",
     "cities":["Berlin","Hamburg","Stuttgart"],
     "total":5},
]
def add_new_country(country_visited,time_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=time_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
add_new_country("Russia",2,["Moscov","Sait Peterburg"])
print(travel_log)