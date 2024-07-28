# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/?envType=company&envId=doordash&favoriteSlug=doordash-thirty-days

# Leetcode 1359
from math import factorial


class Solution:
    def countOrders(self, n: int) -> int:
        # The core of the solution uses combinatorial mathematics.
        # For n pairs of orders, the total number of ways to arrange 2*n items (pickups and deliveries) is (2*n)!
        # (factorial of 2*n).

        # However, since every pickup must precede its corresponding delivery,
        # we need to divide by 2^n to account for the valid permutations.
        # Each pair can be arranged in exactly two ways (valid and invalid),
        # so 2^n ensures we count only the valid sequences.

        mod = 10 ** 9 + 7

        return (factorial(2 * n) // (2 ** n)) % (mod)