# If the heaviest person can share a boat with the lightest person,
# then do so. Otherwise,
# the heaviest person can't pair with anyone, so they get their own boat.


class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans