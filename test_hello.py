from hello import add


def test_add():
    assert add(5, 0) == 5
    assert add(1, -1) == 0
    assert add(100, -1) == 99
