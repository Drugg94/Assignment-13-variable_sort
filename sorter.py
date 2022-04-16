import variable_sort

def add_variable(item, variable):
    """
    Uses an if/else selection to send the input variable to the correct validation method.
    Parameters
    ------------
    variable : str
        Input in str form to be sorted.
    """

    # Comprehensive test case 3
    # Searches for a "." in input. If not found sends to int type conversion
    # If the type conversion errors out then sends the input to string validation.
    test_value = "."
    try:
        if test_value in variable:
            item.float_validation(variable)
        elif int(variable):
            item.int_validation(variable)
    except ValueError:
        item.string_validation(variable)

A = variable_sort.VariableSort

test_variable = input("Please enter a value to be sorted. Type 0 to quit: \n")
while test_variable != "0":
    add_variable(A, test_variable)
    test_variable = input("Please enter a value to be sorted. Type 0 to quit: \n")

print("\nThe sorted lists are as follows:\
    \n\nString - {}\n\nFloats - {}\n\nIntegers - {}".format(A.stringList, A.floatList, A.intList))