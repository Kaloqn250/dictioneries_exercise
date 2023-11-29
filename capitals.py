countries = input().split(', ')
capitals = input().split(', ')

country_info = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in country_info.items():
    print(f'{country} -> {capital}')

