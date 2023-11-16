def collatz(number):
    try:
        if number <= 0:
            raise ValueError
        while number != 1:
            print(number)
            if number % 2 == 0:
                number = int(number / 2)
            else:
                number = int(3 * number + 1)
        else:
            print(number)
            print('Done!')
    except :
        print('invalid')
try:
    input_number = int(input('integer'))
    collatz(input_number)
except ValueError:
    print("invalid")
