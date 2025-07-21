info={
    "Name":"Arona",
    "age":21,
    "subject":"BTECH CSE",
    "marks":[56,60,75,65],
    "SERIAL":("Madhure",21,"Subham",21)
}

print(info)
print(type(info))
print(info["marks"][2])
print(info["SERIAL"])
print(info["subject"][0])

info["Name"]="Subho"
print(info)

#Add new Key:value
info["surname"]="Ram Krishan"
print(info)

#null_dict
null_dict={}
print(null_dict)
null_dict["Name"]="prem"
print(null_dict)