""" Trie in Python based on dict

author: K.Voss
"""


class Trie(object):
    MAGIC_KEY = 'value'

    def __init__(self):
        self.tree = dict()

    def __str__(self):
        return str(self.tree)

    def insert(self, key, val=None):
        node = self.tree
        for c in key:
            parent = node
            node = node.setdefault(c, dict())
        node[self.MAGIC_KEY] = val

    def get(self, key):
        node = self.tree
        for c in key:
            node = node.get(c)
            if not node:
                break
        return node

    def remove(self, key):
        if not self.has(key): return

        node = self.get(key)
        del node[self.MAGIC_KEY]

        rprefixes = reversed([key[:l] for l in range(1,len(key)+1)])
        delk = None
        for rp in rprefixes:
            node = self.get(rp)
            if delk: del node[delk]
            if len(node.keys()) > 0: return
            else: delk = rp[-1]
        del self.tree[delk]

    def has(self, key):
        node = self.get(key)
        if node and self.MAGIC_KEY in node.keys():
            return True
        return False

import unittest
class TestTrie(unittest.TestCase):
    def test_ops(self):
        t = Trie()
        t.insert('ann', 24)
        t.insert('aneta', 25)
        t.insert('monica', 25)

        # self.assertEqual(25, t.get('an'))

        self.assertTrue(t.has('ann'))
        self.assertTrue(not t.has('anna'))

        t.remove('aneta')
        self.assertTrue(not t.has('aneta'))
        t.remove('ann')
        self.assertTrue(not t.has('ann'))

if __name__ == '__main__':
    unittest.main()

