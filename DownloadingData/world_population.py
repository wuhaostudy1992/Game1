import json

with open('population_data.json', 'r') as f:
    pop_data = json.load(f)
    
#Print the data in which year contains character '0'
for pop_dict in pop_data:
    if pop_dict['Year'] == 2005:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name, ':', population)
