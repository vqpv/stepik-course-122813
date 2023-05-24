import json

d = json.loads(input())

print(max(max(d, key=lambda x: x["age"])["age"], max(d, key=lambda x: x["chief"]["age"])["chief"]["age"]))
