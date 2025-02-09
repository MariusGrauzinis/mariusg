
# restaurants = [
#     {"name": "CiliPica", "rating": 4.5},
#     {"name": "SushiExpress", "rating": 3.8},
#     {"name": "BurgerKing", "rating": 4.2},
#     {"name": "DominoPizza", "rating": 4.7},
#     {"name": "ExpresPica", "rating": 3.5},
#     {"name": "KFC", "rating": 4.1},
#     {"name": "FelixChiken", "rating": 3.5},
#     {"name": "WokBusters", "rating": 4.9}
# ]

restaurant_list = []
restaurants_count = int(input("Enter number of restaurants"))
for i in range(restaurants_count):
    restaurant_name = input("Restaurant name:")
    restaurant_rating = float(input("Restaurant rating:"))
    restaurant_list.append({"name": restaurant_name, "rating": restaurant_list})
searching_rating = input("Enter minimum rating")
if searching_rating.isnumeric():
    searching_rating = float(searching_rating)
else:
    searching_rating = 4.0
def filtered_list(restaurant_list, searching_rating):
    filtered_list = []
    for r in restaurant_list:
        if r["rating"] <= searching_rating:
            filtered_list.append(r"name")
        return filtered_list
result = filtered_list(restaurant_list, searching_rating)
print(result)