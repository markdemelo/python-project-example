import package.add as add
import package.extras.multiply as multiply
import package.extras.divide as divide


def print_subtract():
    print('this is from subtract')


if __name__ == "__main__":
    print("\nthese are in the module:")
    print_subtract()
    print("\nthese are from imported modules:")
    add.print_add()
    multiply.print_multiply()
    divide.print_divide()
