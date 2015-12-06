def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

def test_twice():
    assert func(func(4)) == 5