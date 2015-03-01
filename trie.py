
class Trie():
    def __init__(self):
        self.tree = dict()

    def __str__(self):
        return str(self.tree)

    def insert(self, key, val=None):
        node = self.tree
        for c in key:
            parent = node
            node = node.setdefault(c, dict())
        node['value'] = val

    def get(self, key):
        node = self.tree
        for c in key:
            try:
                node = node[c]
            except KeyError:
                node = None
        return node

    def remove(self, key):
        if not self.has(key): return

        node = self.get(key)
        del node['value']

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
        if not node:
            return False
        elif 'value' in node.keys():
            return True
        else:
            return False

def main():
    t = Trie()
    t.insert('ann', 24)
    t.insert('aneta', 25)
    t.insert('monic', 25)
    print t
    assert t.has('ann')
    assert t.has('anna')==False

    t.remove('aneta')
    print t
    t.remove('ann')
    print t

if __name__ == '__main__':
    main()

