class Node:
    def __init__(self) -> None:
        self.child = dict()
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = Node()
            node = node.child[ch]
        node.is_word = True

    def get_prefix(self, word):
        node = self.root
        prefix = []
        for ch in word:
            if ch not in node.child:
                return None
            node = node.child[ch]
            prefix.append(ch)
            if node.is_word:
                return ''.join(prefix)
        return None


class Solution:
    def replace_words(self, dictionary: list[str], sentence: str) -> str:
        trie_obj = Trie()
        for word in dictionary:
            trie_obj.insert_word(word=word)

        output = []
        s_words = sentence.split()
        for s_word in s_words:
            prefix = trie_obj.get_prefix(s_word)
            if prefix:
                output.append(prefix)
            else:
                output.append(s_word)

        return " ".join(output).strip()


dic = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
obj = Solution()
res = obj.replace_words(dic, sentence)
print(f"Res is {res}")
