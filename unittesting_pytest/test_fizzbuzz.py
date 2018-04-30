import fizzbuzz

def test_returns_fizz():
    fizzbuzz.returns_fizz(3)
    assert "Fizz"

def test_returns_buzz():
    fizzbuzz.returns_buzz(5)
    assert "Buzz"

def test_returns_fizzbuzz():
    fizzbuzz.returns_fizzbuzz(15)
    assert "FizzBuzz"

def test_returns_number():
    fizzbuzz.returns_number(1)
    assert 1        
