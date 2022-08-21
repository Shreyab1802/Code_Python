emp = {"A": 2, "Z": 9, "K": 10}

print(sorted(emp.items()))

# output : [('A', 2), ('K', 10), ('Z', 9)]

print(dict(sorted(emp.items())))  #{'A': 2, 'K': 10, 'Z': 9}

print(sorted(emp.items(), key = lambda v:v[1]))

# sorted_val = {k : v for k,v in sorted(emp.items(),key=lambda ,v:v[1])}

dict2 = {"cats": "x" , "tail" : "y"}
input = "CAts"
if input in dict2:
    print(0)
else:
    print(-1)


for i in dict2:
    if i == input.lower():
        dict2[input] = dict2.pop(i)
print(input)


print(dict2)

