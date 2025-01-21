from plates import is_valid
def main():
    test_min_max_characters()
    test_start_with_letters()
    test_number_zero()
    test_number()
def test_min_max_characters():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEGEFH") == False
def test_start_with_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
 

def test_number_zero():
     assert is_valid("CS50") == True
     assert is_valid("CS05") == False
def test_number():
    assert is_valid("123") == False
    assert is_valid("46456") == False
if __name__ == "__main__":
    main()
