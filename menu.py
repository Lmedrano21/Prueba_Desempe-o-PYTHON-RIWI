from features import students
import features

def menu():
    validator = True
    # Print a line of equals signs for visual separation
    print("=" * 40)
    # Print the menu title
    print("                 Menu")
    # Print another line of equals signs for visual separation
    print("=" * 40)
    # Display option 1: Add new student in the system
    print("1- Add new student")
    # Display option 2: Show all student in system
    print("2- Print all students")
    # Display option 3: Look for a specific student
    print("3- Search a student")
    # Display option 4: Change student information
    print("4. Update a student")
    # Display option 5: Remove a student from system
    print("5- Delete a student")
    # Display option 6: Save to CSV
    print("6- Save to CSV")
    # Display option 7: Close the program
    print("7- Exit")
    # Print another line of equals signs for visual separation
    print("=" * 40)
    # Print a blank line for spacing
    print()
    # Start a loop that continues while validator is True
    
    while validator:
        
        # Ask user to enter their choice and convert it to an integer
        try:
            print("---------------------------------------------------------")
            Ejecucion = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid option.")
            continue
        
        
        # Check if user chose option 1
        if Ejecucion == 1:
            # Call the add_product function to add a new product
            features.add_student()
        # Check if user chose option 2
        elif Ejecucion == 2:
            # Call the inventory_print function to display all products
            features.print_students()
            #print_students()
        # Check if user chose option 3
        elif Ejecucion == 3:
            # Call the search_producto function to find a specific product
            features.search_students()
            #features_.search_producto()
        # Check if user chose option 4
        elif Ejecucion == 4:
            features.update_students()
        # Check if user chose option 5
        elif Ejecucion == 5:
            # Call the product_delete function to remove a product
            features.delete_students()
        elif Ejecucion == 6:
            features.send_csv()
        # Check if user chose option 6
        elif Ejecucion == 7:
            # Print a divider line for visual separation
            print("-----------------------------------------------")
            # Display thank you message to the user
            print("Thanks for using our system! Have a great day!")
            # Print another divider line
            print("-----------------------------------------------")
            # Set validator to False to exit the loop and end the program
            validator =  False
        # Handle case when user enters an invalid option
        else:
            # Let user know their choice was not valid
            print("Option not valid")