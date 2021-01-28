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

print(fizzbuzz(16))