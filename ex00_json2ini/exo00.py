import json

with open('sample.json','r') as file:
    data = json.load(file)

data.keys()
data.items()

string = ""
for key in data.keys():
    string = string + "[" + key + "]\n"
    for sub_key in data[key].keys():
        string = string + sub_key + "=" + data[key][sub_key] + "\n"
    string = string + "\n"
print(string)

with open('output.ini', 'w') as file:
    file.write(string)