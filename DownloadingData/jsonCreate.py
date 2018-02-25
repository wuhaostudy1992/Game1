import json
import random
import string

#salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))

title = ['Country Name', 'Country Code', 'Year', 'Value']

results = []
for i in range(300):
    element = {}
    element[title[0]] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    element[title[1]] = ''.join(random.sample(string.ascii_letters, 2))
    element[title[2]] = random.randint(1900, 2018)
    element[title[3]] = random.random() * 10000
    results.append(element)

with open('population_data.json', 'w') as f:
    json.dump(results, f)
