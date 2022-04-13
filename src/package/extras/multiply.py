import package.add as add
import package.subtract as subtract
import package.extras.divide as divide


def print_multiply():
    print('this is from divide')


if __name__ == "__main__":
    print("\nthese are in the module:")
    print_multiply()
    print("\nthese are from imported modules:")
    add.print_add()
    subtract.print_subtract()
    divide.print_divide()
