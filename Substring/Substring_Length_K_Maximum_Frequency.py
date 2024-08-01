
def max_freq_subsstring1(s: str, k: int) -> str:

    if not s or k > len(s) or k == 0:
        return ""

    max_freq = 0
    max_fre_substring = ""
    max_frequency_map = {}

    for i in range(len(s) - k + 1):
        substring = s[i: i+k]

        if substring in max_frequency_map:
            max_frequency_map[substring] += 1
        else:
            max_frequency_map[substring] = 1

        if max_frequency_map[substring] > max_freq:
            max_freq = max_frequency_map[substring]
            max_fre_substring = substring
            print(max_freq, max_fre_substring)


    return max_fre_substring


def max_freq_subsstring2(s: str, k:int) -> str:

    if not s or len(s) < k or k == 0:
        return ""

    max_freq_map = {}


    current_window = s[:k]
    max_freq_map[current_window] = 1
    max_freq = 1
    max_freq_substring = current_window

    for i in range(1, len(s) - k + 1):
        current_window = current_window[1:] + s[i + k -1]

        if current_window in max_freq_map:
            max_freq_map[current_window] += 1
        else:
            max_freq_map[current_window] = 1

        if max_freq_map[current_window] > max_freq:
            max_freq = max_freq_map[current_window]
            max_freq_substring = current_window

    return max_freq_substring

string = 'bbbbbaaaaabbabababa'
k = 5
print(max_freq_subsstring1(string , k))
print(max_freq_subsstring2(string , k))