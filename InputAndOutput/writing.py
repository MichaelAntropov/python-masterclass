# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
# with open("cities.txt", "r") as cities_file:
#     for city in cities_file:
#         cities.append(city.strip("\n"))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Tom Waltz"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title, artist, year)
