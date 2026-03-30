# Riwi Students Management System

A comprehensive students management system for any academy. This system allows you to record, manage, update students with full data validation and CSV import/export capabilities.

## Features

### Core Functionality
- **Add Student** - Record new student with id, name, age, program and status
- **View Students** - Display all students in the students dict
- **Search Student** - Find and display details of specific student
- **Update Student** - Modify student price and/or quantity
- **Delete Student** - Remove students from inventory with confirmation

### Data Management
- **Save to CSV** - Export students to CSV file for backup or sharing
- **Data Validation** - Ensures all inputs are valid:
  - student names. program and status cannot be empty
  - Id, Age must be positive numbers (greater than zero)
- **Error Handling** - User-friendly error messages for invalid inputs

## Requirements

- Python 3.6 or higher
- No external packages required - uses only Python standard library

## Installation

1. Clone the repository
```bash
git clone https://github.com/Lmedrano21/Prueba_Desempe-o-PYTHON-RIWI.git
cd Riwi_Store_Register
```

2. No additional packages required - all dependencies are built-in to Python

## Usage

Run the application:
```bash
python main.py
```

You will see a menu with the following options:
```
1. Add new student      - Add a new item to inventory
2. Print all students   - View all students in inventory
3. Search a student     - Find details of a specific student
4. Update a student     - Modify student information
5. Delete a student     - Remove a student from inventory
6. Save information in CSV - Export inventory to file
7. Exit                 - Close the program
```

### Example Workflow
1. Start the program
2. Choose option 1 to add students
3. Enter student id, name, age, program, and status
4. Choose option 2 to view all students
6. Choose option 6 to save data to CSV before exiting

## Project Structure

- `main.py` - Application entry point that displays welcome message and starts menu
- `menu.py` - Contains the main menu system and user interface
- `features.py` - Core functions for all inventory operations and validation
- `students.csv` - CSV file for storing and loading student data
- `README.md` - This file


## CSV File Format

When saving or loading inventory via CSV, use the following format:

```
id,name,age,program,status
1001942314,LUIS,23,RIWI,Y
1001,luifi,23,ds,y
```

The CSV file must have headers in the first row: `id`, `name`, `age`, `program`, `status`

## Author

Lmedrano21
Coder in Riwi