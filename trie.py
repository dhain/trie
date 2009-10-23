class NeedMore(Exception):
    pass


class Node(object):
    __slots__ = 'parent key nodes value'.split()
    no_value = object()

    def __init__(self, parent, key, nodes, value):
        self.parent = parent
        self.key = key
        self.nodes = nodes
        self.value = value

    @property
    def keypath(self):
        n = self
        keypath = [n.key for n in iter(lambda: n.parent, None) if n.key]
        keypath.reverse()
        keypath.append(self.key)
        return keypath

    def walk(self):
        nodes = [self]
        while nodes:
            node = nodes.pop()
            if node.value is not node.no_value:
                yield node
            nodes.extend(node.nodes[key] for key in sorted(node.nodes, reverse=True))


class Trie(object):
    def __init__(self, root_data=Node.no_value, mapping=()):
        self.root = Node(None, None, {}, root_data)
        self.extend(mapping)

    def extend(self, mapping):
        for k, v in mapping:
            self[k] = v

    def __setitem__(self, k, v):
        n = self.root
        for c in k:
            n = n.nodes.setdefault(c, Node(n, c, {}, Node.no_value))
        n.value = v

    def _getnode(self, k):
        n = self.root
        for c in k:
            try:
                n = n.nodes[c]
            except KeyError:
                raise KeyError(k)
        return n

    def __getitem__(self, k):
        n = self._getnode(k)
        if n.value is Node.no_value:
            if n.nodes:
                raise NeedMore()
            else:
                raise KeyError(k)
        return n.value

    def __delitem__(self, k):
        n = self._getnode(k)
        if n.value is Node.no_value:
            raise KeyError(k)
        n.value = Node.no_value
        while True:
            if n.nodes or not n.parent:
                break
            del n.parent.nodes[n.key]
            n = n.parent

    def children(self, k):
        n = self._getnode(k)
        return dict((k, n.nodes[k].value)
                    for k in n.nodes
                    if n.nodes[k].value is not Node.no_value)

    def __iter__(self):
        for node in self.root.walk():
            yield node.keypath

    def iteritems(self):
        for node in self.root.walk():
            yield node.keypath, node.value

    def itervalues(self):
        for node in self.root.walk():
            yield node.value
