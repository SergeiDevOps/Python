rec = {"name": {"firstname": "Bob’", "lastname": "Smith"}, "job": ["dev", "mgr"],
"age": 25}
print(rec)
rec["name"]
print(rec["name"])
rec["name"]["firstname"]
print(rec["name"]["firstname"])
rec["job"]
print(rec["job"])
rec["job"].append("janitor")
print(rec)
