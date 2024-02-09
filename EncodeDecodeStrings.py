from typing import List


class Codec:
    # //dictMap = {1:"espon",2:"sfedscdv"}
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "HelloShreya".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("HelloShreya")