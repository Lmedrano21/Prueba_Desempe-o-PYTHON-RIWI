


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
    # Display option 6: Close the program
    print("6- Exit")
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
            print("funtion add new student here")
        # Check if user chose option 2
        elif Ejecucion == 2:
            # Call the inventory_print function to display all products
            features_.inventory_print()
        # Check if user chose option 3
        elif Ejecucion == 3:
            # Call the search_producto function to find a specific product
            features_.search_producto()
        # Check if user chose option 4
        elif Ejecucion == 4:
            # Call the product_update function to modify a product
            features_.product_update()
        # Check if user chose option 5
        elif Ejecucion == 5:
            # Call the product_delete function to remove a product
            features_.product_delete()
        # Check if user chose option 6
        elif Ejecucion == 6:
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