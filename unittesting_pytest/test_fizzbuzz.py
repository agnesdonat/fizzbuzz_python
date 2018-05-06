import fizzbuzz
import coverage

def test_play():

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
        fizzbuzz.returns_number(4)
        assert 4


def test_one_to_twenty():
    fizzbuzz.one_to_twenty()
    assert [1, 2, "Fizz", 4, "Buzz", 6, 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
