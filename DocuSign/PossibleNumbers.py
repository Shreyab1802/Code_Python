class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping the digits to their corresponding letters
        digit_mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        combinations = []
        self.backtrack(0, [], digits, digit_mapping, combinations)
        return combinations

    def backtrack(self, index: int, path: List[str], digits: str, letters: dict, combinations: List[str]):
        # If the length of path and digits is same, we have a complete combination
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return

        # Get the list of letters using the index and digits[index]
        possible_letters = letters[digits[index]]

        for letter in possible_letters:
            # Add the current letter to the path
            path.append(letter)
            # Recursively explore the next digit
            self.backtrack(index + 1, path, digits, letters, combinations)
            # Remove the current letter from the path before backtracking to explore other combinations
            path.pop()