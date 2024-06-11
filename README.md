# EncryptixInternship_PythonDevelopement 
## Task1: To Do List
1. ToDoList Class: Manages a list of tasks with methods to add, view, and remove tasks.
2. Adding Tasks: Prompts the user to enter a task and adds it to the list.
3. Viewing Tasks: Displays all tasks in the to-do list with numbering for easy reference.
4. Removing Tasks: Prompts the user to enter the task number to remove, validates the input, and removes the corresponding task if valid.
5. User Interface: Provides a menu with options to add, view, remove tasks, or exit the application. Handles user input and calls appropriate methods from the ToDoList class.

## Task2: Calculator
1. Basic Operations Functions: add(x, y), subtract(x, y), multiply(x, y), and divide(x, y) functions perform basic arithmetic operations and return the result. The divide function includes error handling for division by zero.
2. User Interaction: The main function displays a menu with options to add, subtract, multiply, divide, or exit the calculator.
3. Input Validation: This prompts the user to enter two numbers and checks if the inputs are valid numbers. If not, it informs the user and prompts again.
4. Performing Operations: Based on the user's choice, it calls the corresponding function (add, subtract, multiply, divide) and prints the result of the operation.
5. Exit Option: Provides an option to exit the calculator. If the user selects this option, the program prints an exit message and breaks the loop.

## Task3: Password Generator
1. Define Character Sets: The code defines sets of lowercase letters, uppercase letters, digits, and special characters using the string module.
2. Initial Password Setup: Ensures the password contains at least one character from each set by selecting one random character from each and adding them to the password list.
3. Fill Remaining Length: If the desired password length is greater than 4, it adds more random characters from a combined set of all character types to the password list until the desired length is reached.
4. Shuffle Characters: Shuffle the password list to ensure the characters are in a random order for added security.
5. User Input and Error Handling: Prompts the user for the desired password length, handles invalid input, generates the password using the generate_password function, and prints the generated password. This loop continues until valid input is received.

## Task4: Rock Paper Scissors
1. Computer Choice: The get_computer_choice function randomly selects 'rock', 'paper', or 'scissors' using the random.choice method.
2. Determine Winner: The determine_winner function compares the user's choice with the computer's choice and determines the result: "It's a tie!", "You win!", or "You lose!" based on the rules of Rock-Paper-Scissors.
3. User Interaction: In the main function, the user is repeatedly prompted to enter their choice of 'rock', 'paper', or 'scissors'. The input is converted to lowercase to ensure consistency.
4. Result and Score Tracking: After getting the user's choice and the computer's choice, the result of the game is determined and displayed. The user's and computer's scores are updated based on the result.
5. Play Again: The user is asked if they want to play again. If the user inputs 'yes', the game continues; otherwise, the game ends with a thank-you message and exits the loop.

## Task5: Contact Book
1. Contact Class: Stores contact information: name, phone, email, and address.
2. ContactBook Class: Manages a list of contacts with methods to add, view, search, update, and delete contacts.
3. Adding a Contact: Prompts the user to enter contact details and adds the new contact to the contact list.
4. Viewing and Searching Contacts: Displays all contacts or searches for contacts by name or phone number.
5. Updating and Deleting Contacts: Allows updating contact details or deleting a contact by entering the contact's name.
