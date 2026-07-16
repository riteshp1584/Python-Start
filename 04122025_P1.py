import json

i = 0
while i < 20:
    i += 4
    print(i)

list_1 = []
for r in range(10, 101, 10):
    list_1.append(r)

print(list_1)

def get_person():
    return "John", 30, "Paris"

name, age, city = get_person()

print(name)
print(f"The person's name is {name}, and he is {age} years old, and stays in {city}.")


# 1. Sample data structure (nested dict/list)
data = {
    "user": {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "JSON", "Data Analysis"],
        "active": True
    },
    "scores": [95.5, 87.2, 92.0],
    "metadata": {"version": "1.0", "timestamp": "2025-12-04"}
}

# 2. Serialize (dict -> JSON string) with pretty printing
json_str = json.dumps(data, indent=2)
print("Serialized JSON:")
print(json_str)

print(data["user"]["name"])
print(data["scores"][0])
print(data["metadata"]["version"])

fruits = {"apple", "banana", "grapes", "apple", "strawberry"}
print(fruits) # duplicates automatically removed from sets

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# s1.add(5)
#
# s1.remove(2)
#
# s1.discard(10)


print("Union =", s1 | s2)
print("Intersection =",s1 & s2)
print("Only in S1",s1 - s2)
print("Symmetric Difference =",s1 ^ s2)


