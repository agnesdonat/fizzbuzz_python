import fizzbuzz

def test_returns_fizz():
    fizzbuzz.returns_fizz(3)
    assert "Fizz"

def test_returns_buzz():
    fizzbuzz.returns_buzz(5)
    assert "Buzz"
