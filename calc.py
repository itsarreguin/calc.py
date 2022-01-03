import math


def main():
    menu = """
Python calculator----------------------------------------------------
|                                                                   |
|    1- Addition                    |             4- Division       |
|    -----------------------------------------------------------    |
|    2- Subtraction                 |             5- Power          |
|    -----------------------------------------------------------    |
|    3- Multiplication              |             6- Square root    |
---------------------------------------------------------------------

Choose an option: """

    try:
        option = int(input(menu))
        message = 'The result is:'

        if option > 0 or option < 7:
            if option > 0 and option < 5:
                first_num = int(input('Enter a first number: '))
                second_num = int(input('Enter a second number: '))

                if option == 1:
                    print(f'{message} {first_num + second_num}')
                elif option == 2:
                    print(f'{message} {first_num - second_num}')
                elif option == 3:
                    print(f'{message} {first_num * second_num}')
                elif option == 4:
                    print(f'{message} {first_num % second_num}')

            if option > 4 and option < 7:
                if option == 5:
                    main_num = int(input('Enter a base to get the power: '))
                    power = int(input('Exponent to get power: '))
                    print(f'{message} {main_num**power}')

                elif option == 6:
                    sqr_num = int(input('Enter a number to get square root: '))
                    print(f'{message} {math.sqrt(sqr_num)}')

            else:
                print(' ')
                print('Invalid option')
                main()

    except ValueError:
        print(' ')
        print('Only can introduce numbers')
        return main()

if __name__ == '__main__':
    main()