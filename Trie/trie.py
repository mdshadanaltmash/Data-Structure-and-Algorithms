class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_str(self, word: str) -> None:
        curr = self.root
        for ch in word:
            node = curr.children.get(ch)
            if not node:
                node = TrieNode()
                curr.children.update({ch: node})
            curr = node
        curr.is_word = True
        print("Successfully inserted")

    def search_str(self, word: str) -> bool:
        curr = self.root
        for c in word:
            node = curr.children.get(c)
            if not node:
                return False
            curr = node
        return True if curr.is_word else False


new_trie = Trie()
new_trie.insert_str("Shadan")
new_trie.insert_str("Shadan's")
new_trie.insert_str("Shadab")
print(new_trie.search_str("Shadan's"))
print(new_trie.search_str("Shadab"))
print(new_trie.search_str("shadan"))
