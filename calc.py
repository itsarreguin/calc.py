import math
import os


def main():
    menu = """
Python calculator¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                                                                    |
|    1- Addition                    |              4- Division       |
|    ------------------------------------------------------------    |
|    2- Subtraction                 |              5- Power          |
|    ------------------------------------------------------------    |
|    3- Multiplication              |              6- Square root    |
|--------------------------------------------------------------------|
|                                                                    |
|_____________________________________________________________ 7- Exit

Choose an option: """

    clear = lambda: os.system('clear')

    try:
        option = int(input(menu))
        message = 'The result is:'

        if option > 0 and option < 8:
            if option > 0 and option < 5:
                num_x = int(input('Enter a first number: '))
                num_y = int(input('Enter a second number: '))

                if option == 1:
                    print(f'{message} {num_x + num_y}')
                elif option == 2:
                    print(f'{message} {num_x - num_y}')
                elif option == 3:
                    print(f'{message} {num_x * num_y}')
                elif option == 4:
                    try:
                        print(f'{message} {num_x / num_y}')
                    except ZeroDivisionError:
                        print(' '), clear()
                        print("You can't divide between zero")
                        main()

            if option > 4 and option < 7:
                if option == 5:
                    main_num = int(input('Enter a base to get the power: '))
                    power = int(input('Exponent to get power: '))
                    print(f'{message} {main_num**power}')

                elif option == 6:
                    sqr_num = int(input('Enter a number to get square root: '))
                    print(f'{message} {math.sqrt(sqr_num)}')
            if option == 7:
                print('Close program')
        else:
            print(' '), clear()
            print('Invalid option')
            main()

    except ValueError:
        print(' '), clear()
        print('Only can introduce numbers')
        return main()

if __name__ == '__main__':
    main()