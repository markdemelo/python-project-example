import package.subtract as subtract
import package.extras.multiply as multiply
import package.extras.divide as divide


def print_add():
    print('this is from add')


if __name__ == "__main__":   
    print("\nthese are in the module:")
    print_add()
    print("\nthese are from imported modules:")
    subtract.print_subtract()
    multiply.print_multiply()
    divide.print_divide()