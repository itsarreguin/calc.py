import math
import os


def main():
    menu = """
Python calculator¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                                                                    |
|    1- Sum                         |              4- Division       |
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
        message = 'The result of'


        if option > 0 and option < 8:

            if option > 0 and option < 5:
                num1 = int(input('Enter a first number: '))
                num2 = int(input('Enter a second number: '))

                if option == 1:
                    print(f'{message} {num1} + {num2} is: {num1 + num2}')

                elif option == 2:
                    print(f'{message} {num1} - {num2} is: {num1 - num2}')

                elif option == 3:
                    print(f'{message} {num1} x {num2} is: {num1 * num2}')

                elif option == 4:
                    try:
                        print(f'{message} {num1} / {num2} is: {num1 / num2}')
                    except ZeroDivisionError:
                        clear()

                        print("\n You can't divide between zero")
                        main()

            if option > 4 and option < 7:
                if option == 5:
                    base = int(input('Enter a base to get the power: '))
                    power = int(input('Exponent to get power: '))

                    print(f'{message} {base}**{power} is: {base**power}')

                elif option == 6:
                    sqr_num = int(input('Enter a number to get square root: '))

                    print(f'{message} {sqr_num} is: {math.sqrt(sqr_num)}')

            if option == 7:
                clear()
                print('Closed program')
        else:
            clear()

            print('n\ Invalid option')
            main()

    except ValueError as ve:
        clear()

        print('n\ Only can introduce numbers')
        return main()


if __name__ == '__main__':
    main()