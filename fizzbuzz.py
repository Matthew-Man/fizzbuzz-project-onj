def fizzbuzz(n):
    answer = []
    for x in range(1, n + 1):
        if x%3 == 0 and x%5 == 0:
            answer.append("FizzBuzz")
        elif x%5 == 0:
            answer.append("Buzz")
        elif x%3 == 0:
            answer.append("Fizz")
        else:
            answer.append(x)
    return answer


# Refactored ------------------------------------ have I made it more complex?

def is_multiple_three(n):
    return n % 3 == 0

def is_multiple_five(n):
    return n % 5 == 0

def is_fizzbuzz(n):
    return is_multiple_three(n) and is_multiple_five(n)

def fizzbuzz_refactored(n):
    answer = []
    for x in range(1, n + 1):
        if is_fizzbuzz(x):
            answer.append("FizzBuzz")
        elif is_multiple_five(x):
            answer.append("Buzz")
        elif is_multiple_three(x):
            answer.append("Fizz")
        else:
            answer.append(x)
    return answer


print(fizzbuzz(16))