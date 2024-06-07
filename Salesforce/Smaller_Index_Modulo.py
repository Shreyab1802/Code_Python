input = [3,5,4,5,2,10]
result = []*len(input)

for i in range(len(input)-1):
    result.append(input[i] ** input[i+1])

print(max(result))
print(result.index(max(result)))