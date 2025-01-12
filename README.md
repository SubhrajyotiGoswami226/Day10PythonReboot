Day 10: Simple Calculator in Python

Welcome to **Day 10** of my **100 Days of Python Challenge**!  
Today, I created a **simple calculator program** that can perform basic arithmetic operations interactively.


📝 Project Overview

This Python-based **Simple Calculator** allows users to:
1. Perform basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.
2. Enter numbers and an operator interactively.
3. Handle invalid inputs gracefully, including:
   - Non-numeric entries.
   - Division by zero.


💻 How It Works

1. User Interaction
- The user provides:
  - **Two numbers**: Can be integers or floating-point numbers.
  - **An operator**: '+', '-', '*', or '/'.
2. Error Handling
- **Invalid Number Input**: The program checks if the inputs are valid numbers using:
This ensures that both integers and floats are accepted.
Division by Zero: If the user attempts to divide by zero, the program prevents the operation and displays an error message:
3. Arithmetic Operations
Each operation is handled by a separate function
4. Loop for Continuation
The calculator runs in a loop, allowing multiple calculations until the user chooses to exit


📚 Concepts Applied
Functions: Modularized code for each operation (add, sub, mult, div).
Loops: Used a while loop to keep the calculator running until the user exits.
Input Validation: Ensured robust handling of invalid inputs.
String Manipulation: Checked and processed user input for floating-point validation.
