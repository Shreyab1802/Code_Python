class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def search_words_with_prefix(self, prefix: str):
        node = self.root
        # Traverse the Trie to the end of the prefix
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []  # Prefix not in Trie
        # Use DFS to collect all words starting with the prefix
        return self._dfs_collect_words(node, prefix)

    def _dfs_collect_words(self, node: TrieNode, prefix: str):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._dfs_collect_words(child_node, prefix + char))
        return words

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)