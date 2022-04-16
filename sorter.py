from pickletools import stringnl

class VariableSort:
    """
    Class to build a string, int, and float list and sort inputs

    Attributes
    ------------
    stringList : str
        A list of all strings input

    intList : int
        A list of all ints input

    floatList : float
        A list of all floats input

    Methods
    ------------
    string_validation(test)
        Verifies if test is a string and adds it to stringList
    int_validation(test)
        Verifies if test is an int and adds it to intList
    float_validation(test)
        Verifies if test is a float and adds it to floatList
    """
    stringList = []
    intList = []
    floatList = []

    def string_validation(self, test: str) -> str:
        """
        Checks test agains a list of characters and
        adds test to stringList if test passes.

        Parameters
        ------------
        test : str
            The input to be verified
        """

        # Comprehensive test case 1
        # Utilizes a string to match requirement vs input
        test_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in test:
            if i in test_string:
                continue
            return False
        VariableSort.stringList.append(test)

    def int_validation(self, test: int) -> int:
        """
        Checks test agains a variable contaiing a period and
        adds test to intList as an int, if no period exists.

        Parameters
        ------------
        test : str
            The input to be verified
        """

        # Comprehensive test case 2
        # Searches for a "." inside input, and sends a False if found
        test_character = "."
        if test_character in test:
            return False
        try:
            VariableSort.intList.append(int(test))
        except ValueError:
            print("Test failed non-int insertion attempt in int list")

    def float_validation(self, test: float) -> float:
        """
        Checks test to see if it converts to float and
        adds test to floatList if test passes.
        Otherwise, exception notifies of an error and prematurely ends.

        Parameters
        ------------
        test : str
            The input to be verified
        """

        test_period = "."
        if test_period in test:
            try:
                VariableSort.floatList.append(float(test))
            except ValueError:
                print("Test failed non-float insertion attempt in float list")
        else:
            return False

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

A = VariableSort()

test_variable = input("Please enter a value to be sorted. Type 0 to quit: \n")
while test_variable != "0":
    add_variable(A, test_variable)
    test_variable = input("Please enter a value to be sorted. Type 0 to quit: \n")

print("\nThe sorted lists are as follows:\n\nString \
    - {}\n\nFloats - {}\n\nIntegers - {}".format(A.stringList, A.floatList, A.intList))