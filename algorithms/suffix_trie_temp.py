# Vanilla suffix trie. No compression used.

# Solution from https://colab.research.google.com/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_SuffixTrie.ipynb
class SuffixTrie(object):
    def __init__(self, t):
        """ Make suffix trie from t """
        t += '$' # special terminator symbol
        self.root = {}
        for i in range(0, len(t)-1): # for each suffix
            cur = self.root
            for c in t[i:]: # for each character in i'th suffix
                if c not in cur:
                    cur[c] = {} # add outgoing edge if necessary
                cur = cur[c]

# My solution
class RootNode:
    def __init__(self, child = None):
        self.children = {}
        if child:
            self.children[child] = {}


def build_suffix_trie(word:str, root_node:RootNode):
    word += "\0"
    word_len = len(word)-1
    while word_len != -1:
        suffix = word[word_len:]
        # print("suffix:",suffix)
        prev_node = root_node.children
        for index_char in range(0, len(suffix)-1):
            current_char = suffix[index_char]
            if current_char not in prev_node:
                prev_node[current_char] = {}
            prev_node = prev_node[current_char]
        word_len -= 1
    pprint(root_node.children)

word = "test"
build_suffix_trie("test", RootNode())