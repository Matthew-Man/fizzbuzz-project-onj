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


def fizzbuzz_refactored(n):
    return [1]

print(fizzbuzz(16))