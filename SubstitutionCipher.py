def isSubstitutionCipher(string1: str, string2: str):
    countMap = {}

    if len(string1) != len(string2):
        return False

    for i in range(len(string1)):
        countMap[string1[i]] = 1 + countMap[string1[i]]

    for keys in countMap:
        if countMap[keys] != string2.count[keys]:
            return False

    return True


print(isSubstitutionCipher("abc", "bcc"))