import math


def main():
    menu = """
Python calculator---------------------------------------------
|                                                            |
|    1- Addition                |          2- Subtraction    |
|    ----------------------------------------------------    |
|    3- Multiplication          |          4- Division       |
|    ----------------------------------------------------    |
|    5- Powers                  |          6- Square root    |
--------------------------------------------------------------

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

            if option > 5 and option < 7:
                if option == 5:
                    pass

                if option == 6:
                    sqr_num = int(input('Enter a number to get root: '))
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