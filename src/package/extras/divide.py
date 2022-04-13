import package.add as add
import package.subtract as subtract
import package.extras.multiply as multiply


def print_divide():
    print('this is from divide')


if __name__ == "__main__":
    print("\nthese are in the module:")
    print_divide()
    print("\nthese are from imported modules:")
    add.print_add()
    subtract.print_subtract()
    multiply.print_multiply()
    

