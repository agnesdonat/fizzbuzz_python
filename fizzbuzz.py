def returns_fizz(a):
    if a % 3 == 0:
      return "Fizz"

def returns_buzz(a):
    if a % 5 == 0:
        return "Buzz"

def returns_fizzbuzz(a):
    if a % 15 == 0:
        return "FizzBuzz"

def returns_number(a):
    if a % 3 != 0 and a % 5 != 0  and a % 15 != 0:
        return a
