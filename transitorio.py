def valid_input_age(user_input):
    # Create a variable to control the validation loop
    validate = True
    # Start an infinite loop for validation
    while validate:
        # Try to convert the input to a whole number
        try:
            # Convert user input to an integer
            age = int(user_input)
            # Check if the age is negative
            if age < 0:
                # Tell user that age cannot be negative
                print("ERROR: Age cannot be negative. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student age: ")
            # Check if the age is exactly zero
            elif age == 0:
                # Tell user that age cannot be zero
                print("ERROR: Student age cannot be zero. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student age:: ")
            # Check if the age is empty
            elif age == "":
                # Tell user that age cannot be empty
                print("ERROR: Student age cannot be empty. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student age: ")
            # Check if the age is None (no value)
            elif age is type(None):
                # Tell user that age cannot be None
                print("ERROR: The student age cannot be None. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student age: ")
            # Check if the age is a decimal number instead of an integer
            elif age == type(float):
                # Tell user that age must be a whole number
                print("ERROR: The student age must be an integer. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student age: ")
            # If quantity is valid
            else:
                # Set validate to False to exit the loop
                validate = False
                # Return the valid age
                return age
        # Handle case where user enters text instead of a number
        except ValueError:
            # Tell user that they must enter a number
            print("ERROR: Please enter a valid numeric value for age.")
            # Ask user to try again
            user_input = input("Enter the student age: ")