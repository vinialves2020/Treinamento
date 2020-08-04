
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
            print("x * y")
        elif i =="//":
            print(x // y)
        elif i == "+":
            print(x ** y)
        elif i == "%":
            print(x % y)



def run():
    tipos()
    arit0()


if __name__ == '__Aula01__':
    run()



