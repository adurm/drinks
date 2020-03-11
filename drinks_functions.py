# Function to handle reading a file
def read_file(file_name):
    # Try open the file
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Print all lines in the file
            for line in lines:
                print(line.strip('\n').title())

    # If file is not found, print error message
    except FileNotFoundError as err:
        print("File not found.")


# Function to handle writing a file
def write_file(file_name):
    # If file exists, check if the user really wants to rewrite the file
    try:
        open(file_name)
        user_input = input(f'''
WARNING: You are about to rewrite {file_name} since it already exists.
To confirm this option, type 'confirm'.
Otherwise, go back to the main menu.
''')
        # If user confirms, pass the confirmation stage
        if user_input == 'confirm':
            pass
        # Go back to main menu
        else:
            return

    # If file doesn't exist, write new file as normal
    except FileNotFoundError:
        pass

    # Initialise empty food list and a counter
    food_list = []
    count = 1

    # Keep taking input until the user types 'quit'
    while True:
        user_input = input("Add to order: ")
        if user_input == 'quit':
            break

        # Append order to food list and increment counter
        food_list.append(str(count) + ": " + user_input.lower().capitalize() + "\n")
        count += 1

    # Write into file from food list
    file = open(file_name, 'w')
    for food in food_list:
        file.write(food)


# Function to append file
def append_file(file_name):
    # If file exists, read it
    try:
        file = open(file_name, 'r')
        # Work out what the counter was at when the file was written
        count = int(file.readlines()[-1][0]) + 1
        food_list = []

    # If file doesn't exist, print error message
    except FileNotFoundError:
        print("File not found.")
        return

    # Append file by taking
    file = open(file_name, 'a')

    # Keep taking input until the user types 'quit'
    while True:
        user_input = input("Add to order: ")
        if user_input == 'quit':
            break

        # Append order to food list and increment counter
        food_list.append(str(count) + ": " + user_input.lower().capitalize() + "\n")
        count += 1

    # Write into file from food list
    for food in food_list:
        file.write(food)


def run_program():
    # Keep taking input until the user types 'quit'
    while True:
        user_input = input("Task: ")

        if user_input == 'quit':
            break

        # Ask for file name
        file_name = input("Name of order: ")

        # Write file
        if user_input == 'write':
            write_file(file_name)

        # Read file
        elif user_input == 'read':
            read_file(file_name)

        # Append file
        elif user_input == 'append':
            append_file(file_name)

# TODO: amend crashes when file empty
