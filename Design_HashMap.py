class MyHashMap:

    def __init__(self):
        self.hashMap = [-1] * 10000000

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        self.hashMap[key] = -1
