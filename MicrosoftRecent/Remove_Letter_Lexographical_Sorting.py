class Solution:

    def place_character(self, arr, c):
        low = 0
        high = len(arr) - 1
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > c:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        arr[ans] = c

    def get_min_letters_to_remove(self, s: str) -> int:
        chars = list(s)
        sorted_char_list = []
        size = 0
        for c in chars:
            if size == 0 or c > sorted_char_list[size - 1]:
                sorted_char_list.append(c)
                size += 1
            else:
                self.place_character(sorted_char_list, c)
        return len(s) - size



# Test cases
solution_instance = Solution()
print(solution_instance.get_min_letters_to_remove("banana"))  # Expected output: 3
print(solution_instance.get_min_letters_to_remove("abc"))  # Expected output: 0
print(solution_instance.get_min_letters_to_remove("cba"))  # Expected output: 2
print(solution_instance.get_min_letters_to_remove("aabbcc"))  # Expected output: 3
print(solution_instance.get_min_letters_to_remove("abacbd"))  # Expected output: 2
