
def returns_fizzbuzz(a):
    if a % 15 == 0:
        return True

def returns_fizz(a):
    if a % 3 == 0:
      return True

def returns_buzz(a):
    if a % 5 == 0:
        return True

def returns_number(a):
    if a % 3 != 0 and a % 5 != 0  and a % 15 != 0:
        return True

def play(a):
    if returns_fizzbuzz(a):
        return "FizzBuzz"
    if returns_fizz(a):
        return "Fizz"
    if returns_buzz(a):
        return "Buzz"
    else:
        returns_number(a)
        return a

def one_to_twenty():
    list = []
    for a in range(1,21):
        list.append(play(a))
    return list

print(one_to_twenty())
