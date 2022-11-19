import json

# Opening JSON file
f = open('./i18n/es/words.json')

# returns JSON object as
# a dictionary
data = json.load(f)

print(data['hi'])

# Closing file
f.close()