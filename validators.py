def validate_user_input(message, max_len=0, options=None):
    """
    Validates user input based on certain criteria.

    Parameters:
    - message (str): The prompt message to display to the user.
    - max_len (int): The maximum length allowed for the input. If provided, the input length must not exceed this value.
                     Default is 0, indicating no maximum length constraint.
    - options (list or None): A list of valid options. If provided, the input must be one of these options.
                              Default is None, indicating no specific options constraint.

    Returns:
    - str: The validated user input that satisfies the specified criteria.

    Notes:
    - The function continues prompting the user until valid input is provided.
    - It handles numeric input only.
    - If `max_len` is specified, the input length is checked against it.
    - If `options` are specified, the input is checked against these options.
    - If input doesn't meet the specified criteria, appropriate error messages are displayed.
    """
    user_input=""
    while True:
        user_input = input(message)
        try:
            int(user_input)
            if max_len and len(user_input)<=max_len:
                return user_input
            elif max_len and len(user_input)>=max_len:
                print(f"\033[1;91mThe numbered you entered has too many digits, the maximum amount of digits is {max_len}\033[00m")
            elif options and int(user_input) in options:
                return user_input
            elif options and int(user_input) not in options:
                print(f"\033[1;91m{user_input} is not a valid option, the valid options are: {options}\033[00m")
            elif not max_len and not options:
                return user_input
        except ValueError:
            print("\033[1;91mPlease enter numbers only\033[00m")


def validate_number_range(message, min_val, max_val):
    """
    Validates user input to ensure it falls within a specified numeric range.

    Parameters:
    - message (str): The prompt message to display to the user.
    - min_val (int): The minimum allowed value for the input.
    - max_val (int): The maximum allowed value for the input.

    Returns:
    - int: The validated user input that falls within the specified range.

    Notes:
    - The function continues prompting the user until valid input is provided.
    - It handles numeric input only.
    - The input is checked against the specified minimum and maximum values.
    - If the input value is less than `min_val`, an error message is displayed.
    - If the input value is greater than `max_val`, an error message is displayed.
    - If the input is not a valid number, an appropriate error message is displayed.
    """
    user_input=""
    while True:
        user_input = input(message)
        try:
            int(user_input)
            if int(user_input)<min_val:
                print(f"\033[1;91mThe number you entered is too small, your value should be greater than or equal to {min_val}\033[00m")
            elif int(user_input)>max_val:
                print(f"\033[1;91mThe number you entered is too big, your value should be less than or equal to {max_val}\033[00m")      
            else:
                return int(user_input)
        except ValueError:
            print("\033[1;91mPlease enter numbers only\033[00m")


if __name__=="__main__":
    # id = validate_user_input("Please enter your id number: ", 10)
    # option = validate_user_input("Please enter one of the options: ",options=(1,2,3))
    # an_integer = validate_user_input("Please enter an integer: ")
    # print(id)
    # print(option)
    # print(an_integer)
    validate_number_range("Please enter your age: ", 16, 26)