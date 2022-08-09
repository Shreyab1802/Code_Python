class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1 = s1.split(" ")
        s2 = s2.split(" ")
        s3 = []
        dictA = {}
        dictB = {}

        for i in s1:
            if i in dictA:
                dictA[i] += 1
            else:
                dictA[i] = 1

        for i in s2:
            if i in dictB:
                dictB[i] += 1
            else:
                dictB[i] = 1

        for i in dictA:
            if dictA[i] == 1 and i not in dictB:
                s3.append(i)
        for i in dictB:
            if dictB[i] == 1 and i not in dictA:
                s3.append(i)
        return s3