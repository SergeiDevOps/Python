D = {"food": "Apple", "quantity": 4, "color": "Red"}
print(D,type(D))
D["food"]
print(D["food"],type(D))
D["quantity"] += 10
print(D["quantity"],type(D))
dp = {}
s = "firstName age"
f = s.split()
dp["firstName"] = f[0] = input("Enter the firstname:  ")
dp["age"] = f[1] = input("Enter the age: ")
print(dp,type(dp))
