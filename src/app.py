# app.py
# test
def add(a, b):
    print("executing addition test case")
    return a + b

def test_add():
    assert add(2, 2) == 4
    assert add(1, 4) == 5
