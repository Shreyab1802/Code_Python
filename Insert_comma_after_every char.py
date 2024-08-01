string_data = "ABC"

def insert_commas_between_letters(s: str) -> str:
    if not s:
        return s
    return ','.join(s)