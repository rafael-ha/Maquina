# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Maquina import Maquina
from MaquinaMecanica import MaquinaMecanica
#from MaquinaElectrica import MaquinaElectrica


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    m1=Maquina("test", "test2")
    print(m1)

    m2=MaquinaMecanica("teest","tests")
    print(m2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
