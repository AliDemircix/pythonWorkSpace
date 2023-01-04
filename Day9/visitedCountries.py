visited_Countries = [
    {"country": "Turkey", "cities": [
        "Ankara", "Istanbul", "Izmir"], "visited":10},
    {"country": "Netherland", "cities": [
        "Leiden", "Amsterdam", "Rotterdam"], "visited":4}
]

def add_new_country(country,cities,visited):
    newCountry= {
        "country":country,
        "cities":cities,
        "visited":visited
    }
    visited_Countries.append(newCountry)
    print(visited_Countries)

add_new_country("Russia",["Moscow","Kubinka"],8)

for country in visited_Countries:
    if country["country"]=="Russia":
        print(country)

# title case 

titleContent = "this sentence's all word will begin capital letter."
print(titleContent.title())