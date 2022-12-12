from second_largest import second_largest

def test_positive():
    ret_val = second_largest([4, 67, 2, 6, 1])
    assert ret_val == 6
    ret_val = second_largest([1, 2, 3, 4, 5, 6])
    assert ret_val == 5
    ret_val = second_largest([6, 5, 4, 3, 2, 1])
    assert ret_val == 5

def test_equal_elems():
    ret_val = second_largest([1, 1, 1, 1])
    assert ret_val is None
    ret_val = second_largest([1, 2, 1, 2])
    assert ret_val == 1
    ret_val = second_largest([6, 5, 4, 3, 2, 1])
    assert ret_val == 5
