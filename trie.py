
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
        node['parent'] = parent

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

        rprefixes = reversed([key[:l] for l in range(1,len(key)+1)])
        for rp in rprefixes:
            node = self.get(rp)
            if rp == key: del node['value']
            if len(node.keys()) > 0:
                return

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
    print t
    assert t.has('ann')
    assert t.has('anna')==False

    t.remove('ann')
    print t

if __name__ == '__main__':
    main()

