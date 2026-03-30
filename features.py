students = {} #this dict is to print and save information about all students, is local
students_for_csv = [] #this is a list to send informato to CSV file with a specific format
def validate_input_student_name(user_input):
    # Start a loop that continues while the input is empty
    while user_input.strip() == "":
        # Tell user that student name cannot be empty
        print("ERROR: Student name cannot be empty. Please enter a valid student name.")
        # Ask user to enter the student name again
        user_input = input("Enter the name of the Student: ")
    # Return the student name after removing extra whitespace
    return user_input.strip()

def validate_input_id(user_input):
    # Create a variable to control the validation loop
    validate = True
    # Start an infinite loop for validation
    while validate:
        # Try to convert the input to a whole number
        try:
            # Convert user input to an integer
            id = int(user_input)
            # Check if the id is negative
            if id < 0:
                # Tell user that ID cannot be negative
                print("ERROR: Id cannot be negative. Please enter a valid age.")
                # Ask user to try again
                user_input = input("Enter the student ID: ")
            # Check if the ID is exactly zero
            elif id == 0:
                # Tell user that ID cannot be zero
                print("ERROR: Student ID cannot be zero. Please enter a valid ID.")
                # Ask user to try again
                user_input = input("Enter the student ID:: ")
            # Check if the ID is empty
            elif id == "":
                # Tell user that ID cannot be empty
                print("ERROR: Student ID cannot be empty. Please enter a valid ID.")
                # Ask user to try again
                user_input = input("Enter the student ID: ")
            # Check if the ID is None (no value)
            elif id is type(None):
                # Tell user that ID cannot be None
                print("ERROR: The student ID cannot be None. Please enter a valid ID.")
                # Ask user to try again
                user_input = input("Enter the student ID: ")
            # Check if the ID is a decimal number instead of an integer
            elif id == type(float):
                # Tell user that ID must be a whole number
                print("ERROR: The student ID must be an integer. Please enter a valid ID.")
                # Ask user to try again
                user_input = input("Enter the student ID: ")
            # If age is valid
            else:
                # Set validate to False to exit the loop
                validate = False
                # Return the valid ID
                return id
        # Handle case where user enters text instead of a number
        except ValueError:
            # Tell user that they must enter a number
            print("ERROR: Please enter a valid numeric value for ID.")
            # Ask user to try again
            user_input = input("Enter the student ID: ")
            
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
            # If age is valid
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
            
def validate_input_student_program(user_input):
    # Start a loop that continues while the input is empty
    while user_input.strip() == "":
        # Tell user that student name cannot be empty
        print("ERROR: Student program cannot be empty. Please enter a valid student program.")
        # Ask user to enter the student name again
        user_input = input("Enter the name of the Student: ")
    # Return the student name after removing extra whitespace
    return user_input.strip()

def validate_input_student_status(user_input):
    # Start a loop that continues while the input is empty
    while user_input.strip() == "":
        # Tell user that student status cannot be empty
        print("ERROR: Student status cannot be empty. Please enter a valid student status.")
        # Ask user to enter the student status again
        user_input = input("Enter the status of the Student: (y== for active, n== for inactive)")
    # Return the student staus after removing extra whitespace
    return user_input.strip()

def add_student():
    # Create an empty dictionary to hold the new student
    student_added_to_saved = {}
    # Use try-except to handle any errors during input
    try:
        # Ask user to enter the student id
        student_id = input("Enter the id of the student: ")
        # Validate the student id to ensure it is valid
        student_id = validate_input_id(student_id)
        
        # Ask user to enter the student name
        student_name = input("Enter the name of the student: ")
        # Validate the student name to ensure it is not empty
        student_name = validate_input_student_name(student_name)
    

        # Ask user to enter the student age
        age = input("Enter the student age: ")
        # Validate the age to ensure it is valid
        age = valid_input_age(age)
        
        # Ask user to enter the student program
        program = input("Enter the student program: ")
        # Validate the program to ensure it is valid
        program = validate_input_student_program(program)
        
        # Ask user to enter the student status
        status = input("Enter the student status: (y== for active, n== for inactive): ")
        # Validate the status to ensure it is valid
        status = validate_input_student_status(status)
        
        
        # Add the student to a temporary dictionary with student name as the key
        student_added_to_saved[student_name] = {
            # Store the student name
            "name": student_name,
            # Store the student id
            "id": student_id,
            # Store the student age
            "age": age,
            #Store the student program
            "program": program,
            #Store the student status
            "status": status
        }
        # Add the new student to the main students dictionary
        students.update(student_added_to_saved)
        
        # Create another dictionary with the same student info for CSV saving
        student_added_to_saved_csv = {
            # Store the student name
            "name": student_name,
            # Store the student id
            "id": student_id,
            # Store the student age
            "age": age,
        }
        
        # Add the student to the list that will be saved to CSV
        students_for_csv.append(student_added_to_saved_csv)
        # Display the current list of items to be saved (for debugging)
        for key, student in student_added_to_saved.items():
            print("---------------------------------------------------------")
            print(f"student to save: {student['name']}, id: {student['id']}, age: {student['age']}, program: {student['program']}, status: {student['status']}")
        # Tell user that the student was added successfully
        print("student added successfully")
        print("---------------------------------------------------------")
        # Exit the function
        return
    # Handle any value errors if invalid data is entered
    except ValueError:
        # Tell user that id and age must be valid numbers
        print("ERROR: Please enter valid numeric values for id and age.")
