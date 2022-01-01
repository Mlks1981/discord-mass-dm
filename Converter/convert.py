#Mlks1981
import json

with open("ids.json", "r") as file:
  data = json.load(file)
with open('ids.txt') as f:
    lines = f.readlines()
    for line in lines:
      id = line.replace('\n', '')
      if id in data:
        print(f'avoiding duplicate: {id}')
      else:
       id = line.replace('\n', '')
       data.append(id)
       print(f"{id} was succuessfully added")
       with open("ids.json", "w") as file:
          json.dump(data, file) 
f.close()
