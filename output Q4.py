stateCapital={"AndhraPradesh":"Hyderabad","Bihar":"Patna","Maharastra":"Mumbai","Rajasthan":"Jaipur"}

print(stateCapital.get("Bihar"))
print(stateCapital.keys())
print(stateCapital.values())
print(stateCapital.items())
print(len(stateCapital))
print("Maharastra" in stateCapital)
print(stateCapital.get("Assam"))
del stateCapital["AndhraPradesh"]
print(stateCapital)

