# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def tipos():
    i = 10
    s = "10"
    f = 10.0
    b = False
    print(f'{type(i)} {type(s)} {type(f)} {type(b)}')


def arit0(x, y):
    op = '+ - / * // ** %'.split()

    for i in op:
        if i == "+":
            print(x + y)
        elif i == "-":
            print(x - y)
        elif i == "/":
            print(x / y)
        elif i == "*":
            print(x*y)
        elif i =="//":
            print(x // y)
        elif i == "+":
            print(x ** y)
        elif i == "%":
            print(x % y)



def run():
    tipos()
    arit0(4, 5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
