from Square import get_square
def test_number_square():
    x = 5
    res = get_square(x)
    assert res == 25

def test_float_square():
    x = 3.5
    res = get_square(x)
    assert res == 12.25

def test_negative_square():
    x = -4
    res = get_square(x)
    assert res == 16
    

 