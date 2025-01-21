from bank import value
def main():
    test_return_zero()
    test_case()
    test_phrase()


def test_return_zero():
    assert value("hello") ==  0
    assert value("Hello, Newman") == 0

def test_case():
    assert value("hey") == 20
    assert value("Hi!") == 20
def test_phrase():
    assert value("What's up?") == 100
    assert value("Good morning!") == 100
if __name__ == "__main__":
    main()
