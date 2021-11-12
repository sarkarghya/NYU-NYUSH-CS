import json

data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }

json_data = json.dumps(data)
print (type(json_data))
print (json_data)

original_data = json.loads(json_data)
print (type(original_data))
print (original_data)
