import re


def is_word_in_dictionary(word, dictionary):
    # Convert the word with * and . to a regex pattern
    pattern = word.replace('*', '.*')

    # Compile the regex pattern
    regex = re.compile(f"^{pattern}$")

    # Check if any word in the dictionary matches the pattern
    for dict_word in dictionary:
        if regex.match(dict_word):
            return True

    return False


# Example usage
dictionary = ["apple", "banana", "grape", "orange", "watermelon"]
word = "a*le"  # Should match "apple"
print(is_word_in_dictionary(word, dictionary))  # Output: True

word = "b.n.n."  # Should match "banana"
print(is_word_in_dictionary(word, dictionary))  # Output: True

word = "w*melon"  # Should match "watermelon"
print(is_word_in_dictionary(word, dictionary))  # Output: True

word = "o*gr.pe"  # Should not match any word
print(is_word_in_dictionary(word, dictionary))  # Output: False
