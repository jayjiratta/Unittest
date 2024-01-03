def FizzBuzz (numbers) :
    for num in numbers :
        if num % 3 == 0 and num % 5 == 0 :
            return ('FizzBuzz')
        else :
            if num % 3 == 0 :
                return ('Fizz')
            if num % 5 == 0 :
                return ('Buzz')