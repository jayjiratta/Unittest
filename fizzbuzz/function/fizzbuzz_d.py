def get_fizzbuzz (num) :
    if num % 3 == 0 and num % 5 == 0 :
        return 'FizzBuzz'
    elif num % 3 == 0 :
        return 'Fizz'
    elif num % 5 == 0 :
        return 'Buzz'
    return ""

if __name__ == "__main__" :
    print(get_fizzbuzz(5))