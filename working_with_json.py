import json
import requests as rq

data = {
    "name":"some_name",
    "age":35,
    "Gender":"Male",
    "employers":{
        "emp.name":"John",
        "emp.age":25
    }
}

# Serialization (writing / dumping)
with open("test_json.json", 'w') as file:
    json.dump(data, file)

# Deserialization (reading / loading)
with open("test_json.json", 'r') as file:
    data = json.load(file)

print (f"loaded data is of type {type(data)}")

# Writing to a python string using dumps(data, indent=int, seperator=tuple)

data_as_string = json.dumps(data, indent=4)
# print (data_as_string)
# Basic Example
response = rq.get("https://jsonplaceholder.typicode.com/todos")
print (type(response))
data_new = json.loads(response.text)
print (f"Loaded data type: {type(data_new)}")
print (data_new[0])
print (data_new[1])

# finding users with most completed tasks
todo_by_user = {}
# recording number of tasks completed
for todo in data_new:
    if todo['completed']:
        try:
            todo_by_user[todo["userId"]] +=1
        except KeyError:
            todo_by_user[todo["userId"]] = 1

# the key arguement tells the sorted function which "value" should it sort by
top_users = sorted(todo_by_user.items(), key=lambda x: x[1], reverse=True)
print (f"User {top_users[0][0]} has the most completed taks of {top_users[0][1]}")

# filtering all completed tasks and writing to file
# defining our filter function
def is_completed(todo):
    return todo["completed"]

# the filter function runs of every item inside a list, and appends it to the output list if the function passed
# to it (is_completed) returns True
completed_tasks = list(filter(is_completed, data_new))
with open("completed_tasks.json", 'w') as file:
    json.dump(completed_tasks, file, indent=4)
