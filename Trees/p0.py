#3093. Longest Common Suffix Queries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        
        root = TrieNode()

        # Function to update best candidate
        def update(node, idx):
            word_len = len(wordsContainer[idx])

            if (word_len < node.best_length or
               (word_len == node.best_length and idx < node.best_index)):
                
                node.best_length = word_len
                node.best_index = idx

        # Build Trie using reversed words
        for idx, word in enumerate(wordsContainer):
            rev_word = word[::-1]

            node = root
            update(node, idx)

            for ch in rev_word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                update(node, idx)

        ans = []

        # Process queries
        for query in wordsQuery:
            rev_query = query[::-1]

            node = root

            for ch in rev_query:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_index)

        return ans
