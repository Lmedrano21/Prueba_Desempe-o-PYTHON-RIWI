import csv
import os
global students, students_for_csv
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
    validator = True
    while validator:
        if user_input == "a" or user_input == "i":
            validator = False
            return user_input
        else:
            print("ERROR: Student status input is not valid. Please enter a valid student status.")
            user_input = input("Enter the status of the Student: (a== for active, i== for inactive: ").lower()

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
        status = input("Enter the status of the Student: ('a' -> for active, or 'i' -> for inactive: ").lower()
        # Validate the status to ensure it is valid
        status = validate_input_student_status(status)
        
        
        # Add the student to a temporary dictionary with student name as the key
        student_added_to_saved[student_id] = {
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
        # Display the current list of items to be saved (for debugging)
        for key, student in student_added_to_saved.items():
            print("---------------------------------------------------------")
            print(f"Student to save: {student['name']}, id: {student['id']}, age: {student['age']}, program: {student['program']}, status: {student['status']}")
        # Tell user that the student was added successfully
        print("Student added successfully.")
        print("---------------------------------------------------------")
        # Exit the function
        return
    # Handle any value errors if invalid data is entered
    except ValueError:
        # Tell user that id and age must be valid numbers
        print("ERROR: Please enter valid numeric values for id and age.")

def print_students():
    # Create an empty dictionary for displaying students
    total_student = {}
    # Copy all students from students into total_students
    total_student.update(students)
    # Print a divider line for visual separation
    print("---------------------------------------------------------")
    # Print a header message
    print("Here are your students list")
    # Loop through each student in the dict
    for student, details in total_student.items():
        # Print the student ID
        print(f"Id: {student}")
        # Print the student name
        print(f"Name: {details['name']}")
        # Print the student age 
        print(f"Age: {details['age']}")
        # Print the student program
        print(f"Program: {details['program']}")
        # Print the student status
        print(f"Status: {details['status']}")
        print("")
    # Print a divider line for visual separation
    print("---------------------------------------------------------")

    return

def search_students():
    validador = True
    
    while validador:
        try:
            # Ask user to enter the id of the student they want to find
            id_to_search = int(input("Please input the id of the student to search: "))
            # Try to find the student in the students dictionary
            student_info = students.get(id_to_search)
            # Check if the student was found
            if student_info:
                # Print a header for the student information
                print("---------------------------------------------------------")
                print(f"Student's Information: ")
                # Print the ID
                print(f"Id: {student_info['id']}")
                # Print the student name
                print(f"Name: {student_info['name']}")
                # Print the student age
                print(f"Age: {student_info['age']}")
                # Print the student program
                print(f"program: {student_info['program']}")
                # Print the student status
                print(f"status: {student_info['status']}")
                # Print a divider line
                print("---------------------------------------------------------")
                validador = False
            # If student was not found
            else:
                # Tell user that the student does not exist
                print(f"The student '{id_to_search}' is not found, please try again.")
                # Print a divider line
                validador = False
                print("---------------------------------------------------------")
        except ValueError:
            print("ERROR: Please enter a valid numeric value for id.")

def update_students():
    validador = True
    
    while validador:    
        
        try:  
            # Ask user to enter the id of the student they want to find
            id_to_search = int(input("Please input the id of the student to update: "))
            # Try to find the student in the students dictionary
            student_info = students.get(id_to_search)
            if not student_info:
                # Tell user that the student does not exist
                print("The student does not exist.")
                validador = False
                continue
            # Print current product information
            print(f"\nUpdate: {student_info['id']}, name: {student_info['name']}, age: {student_info['age']}, program: {student_info['program']}, status: {student_info['status']})")
            # Print option 1 to change the name
            print("1. Change Name")
            # Print option 2 to change the age
            print("2. Change Age")
            # Print option 3 to change Program
            print("3. Change Program")
            # Print option 4 to change Status
            print("4. Change Status")
            
            # Ask user which update option they want to choose
            option = input("Choose an option: ")

            # Check if user chose option 1
            if option == "1":
                # Ask for new name and update it
                student_info["name"] = input("New name: ")
            # Check if user chose option 2
            elif option == "2":
                # Ask for new age quantity and update it
                student_info["age"] = int(input("New Age: "))
            # Check if user chose option 3
            elif option == "3":
                # Ask for new program and update it
                student_info["program"] = input("New program: ")
            elif option == "4":
                # Ask for new status quantity and update it
                student_info["status"] = input("New Status: ")
            # Handle invalid option
            else:
                # Tell user they selected an invalid option
                print("Invalid option.")
                
            # Tell user that the update was successful
            print("Update successful.")
            validador= False
            # Exit the function
            return
        except ValueError:
            print("ERROR: Please enter a valid numeric value for id.")

def delete_students():
    validator = True
     
    while validator:
        try:
        
            # Ask user to enter the ID of the student they want to delete
            id = int(input("Enter the id of the student you wish to delete: "))
            # Check if the product exists in the inventory
            if id in students:
                # Ask user to confirm they want to delete the student
                confirmar = input(f" Are you sure you want to delete '{id}'? (Yes/No): ").lower()  
                # Check if user confirmed by typing 'yes'
                if confirmar == 'yes':
                    # Remove the student from the students dictionary
                    del students[id]
                    # Tell user that the student was deleted successfully
                    print(f" The student '{id}' has been successfully deleted.")
                    # Exit the function
                    validator = False
                    return
                # If user did not confirm
                else:
                    # Tell user that the operation was cancelled
                    print(" Operation cancelled by the user")
                    validator = False
                    # Exit the function
                    return
            # If the student does not exist in students
            else:
                # Tell user that the studend was not found
                print(f" Error: The student '{id}' does not exist in the system.")
                validator = False
                # Exit the function
                return
        except ValueError:
            print("ERROR: Please enter a valid numeric value for id.")

def send_csv():
    for student in students:
        students_for_csv.append(students[student])
    # Set the filename where data will be saved
    csv_filename = "students.csv"
    # Create a list of column names for the CSV file
    fieldnames = ["id", "name", "age", "program", "status"]
    # Use try-except to handle file writing errors
    try:
        # Check if the CSV file exists and is not empty
        file_exists = os.path.isfile(csv_filename) and os.path.getsize(csv_filename) > 0
        
        # Open the CSV file in append mode (add data to the end)
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            # Create a CSV writer that will write dictionaries as rows
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
            
            # If the file is new, write the column headers
            if not file_exists:
                # Write the header row with column names
                writer.writeheader()
            # Write all the products from inventory_for_csv list to the file
            writer.writerows(students_for_csv)
            
        # Tell user that the file was saved successfully
        print("CSV file is saved successfully")
        # Clear the list since data has been saved
        students_for_csv.clear()
        
    # Handle any errors that occur during file writing
    except Exception as e:
        # Display the error message to the user
        print(f"Error saving CSV: {e}")