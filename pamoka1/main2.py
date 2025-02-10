def fitered_list(rest_list: list[dict[str, str | float]], min_search_rating: float) -> list[str]:
    for entry in rest_list:
        if entry["rating"] >= min_search_rating:
            filtered_list.append(entry["name"])
    return filtered_list


filtered_list = []
rest_list = []
rest_count = int(input("Enter the number of restorants:" ))
for i in range(rest_count):
    rest_name = input("Restorant name: ")
    rest_rating = float(input("Restorant rating "))
    rest_list.append({"name": rest_name, "rating": rest_rating}) 
min_search_rating = float(input("Enter the minimum rating: "))
if min_search_rating.isnumeric():
    min_search_rating = float(min_search_rating)
else:
    min_search_rating = 4.0    
resul = fitered_list(rest_list, min_search_rating)
resul.sort()
print(resul)
 