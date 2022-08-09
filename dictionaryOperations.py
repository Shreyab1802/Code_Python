emp = {"A": 2, "Z": 9, "K": 10}

print(sorted(emp.items()))

# output : [('A', 2), ('K', 10), ('Z', 9)]

print(dict(sorted(emp.items())))  #{'A': 2, 'K': 10, 'Z': 9}

print(sorted(emp.items(), key = lambda v:v[1]))

# sorted_val = {k : v for k,v in sorted(emp.items(),key=lambda ,v:v[1])}