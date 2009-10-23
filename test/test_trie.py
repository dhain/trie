from nose.tools import *

import trie


def test_root_no_value():
    t = trie.Trie()
    assert_raises(KeyError, t.__getitem__, ())


def test_root_with_value():
    t = trie.Trie('hello')
    assert t[()] == 'hello'


def test_setitem():
    t = trie.Trie()
    t['foo'] = 'bar'
    assert t['foo'] == 'bar'


def test_needmore():
    t = trie.Trie()
    t['foo'] = 'bar'
    assert_raises(trie.NeedMore, t.__getitem__, 'fo')


def test_keyerror():
    t = trie.Trie()
    assert_raises(KeyError, t.__getitem__, 'foo')


def test_delitem():
    t = trie.Trie()
    t['foo'] = 'bar'
    del t['foo']
    assert_raises(KeyError, t.__getitem__, 'foo')
    assert not t.root.nodes


def test_delitem_keyerror():
    t = trie.Trie()
    assert_raises(KeyError, t.__delitem__, 'foo')
    t['foobar'] = 'bar'
    assert_raises(KeyError, t.__delitem__, 'foo')


def test_children():
    t = trie.Trie()
    t['foo'] = 'bar'
    t['fox'] = 'baz'
    assert not t.children('f')
    assert t.children('fo') == {'o': 'bar', 'x': 'baz'}


def test_iter():
    t = trie.Trie()
    t['f'] = 'fval'
    t['foo'] = 'fooval'
    t['bar'] = 'barval'
    t['baz'] = 'bazval'
    itered = list(t)
    assert itered == map(list, 'bar baz f foo'.split()), itered


def test_iteritems():
    t = trie.Trie()
    t['f'] = 'fval'
    t['foo'] = 'fooval'
    t['bar'] = 'barval'
    t['baz'] = 'bazval'
    itered = list(t.iteritems())
    assert itered == zip(map(list, 'bar baz f foo'.split()), 'barval bazval fval fooval'.split()), itered


def test_itervalues():
    t = trie.Trie()
    t['f'] = 'fval'
    t['foo'] = 'fooval'
    t['bar'] = 'barval'
    t['baz'] = 'bazval'
    itered = list(t.itervalues())
    assert itered == 'barval bazval fval fooval'.split(), itered
