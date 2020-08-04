# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    i=10
    s="10"
    f=10.0
    b=False
    print(type(i))
    print(type(s))
    print(type(f))
    print(type(b))
    n =input("Qual teu nome? ")
    if n:
       name = n
    print(f'Hi, {name}')
    # print(f'Hi, {name}')
def tipos():
    i = 10
    s = "10"
    f = 10.0
    b = False
    print(f'{type(i)} {type(s)} {type(f)} {type(b)}')


def arit0():
    print(4 + 5)


def run():
    tipos()

    arit0()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
