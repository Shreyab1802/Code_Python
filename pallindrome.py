def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    string1 = ""
    string2 = ""

    if len(s) == 0 | 1:
        return True

    for i in s:
        if i.isalnum():
            string1 += i
    print(string1)

    for j in string1[::-1]:
        string2 += j
    print(string2)

    return string1 == string2