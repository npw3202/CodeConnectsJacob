import pytest
from map_impl import *

def test_insert():
    # add, get
    # m.put("key", "value")
    # value = m.get("key")
    m = MyMap()
    m.put("hello", "world")
    assert "world" == m.get("hello")

def test_evil_insert():
    # add, get
    # m.put("key", "value")
    # value = m.get("key")
    m = MyMap()
    m.put("hello", "world")
    m.put("world", "hello")
    assert "world" == m.get("hello")