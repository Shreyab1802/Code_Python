class Solution:
    def BitsToNumber(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)
        return int(n,2)


# Input : 00000010100101000001111010011100
# Output : 43261596 (00000010100101000001111010011100)