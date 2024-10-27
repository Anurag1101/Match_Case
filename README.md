# Day of the Week Program with Match-Case and Input Validation

This Python script prompts the user to enter a number between 1 and 7, using the `match-case` statement (similar to a switch-case) to display the corresponding day of the week. It includes input validation to handle incorrect or out-of-range inputs, providing a user-friendly experience.

## Features
- **Match-Case Logic**: Implements Python's `match-case` structure to map numbers to days.
- **Input Validation**: Ensures user input is an integer within the specified range (1-7).
- **Error Handling**: Provides meaningful error messages for out-of-range or non-integer inputs.

## How to Use
1. Run the script.
2. Enter a number between 1 and 7 when prompted:
   - `1` -> Monday
   - `2` -> Tuesday
   - `3` -> Wednesday
   - `4` -> Thursday
   - `5` -> Friday
   - `6` -> Saturday
   - `7` -> Sunday
3. If the input is valid, the program outputs the corresponding day of the week.
4. If the input is out of range, an error message will prompt you to enter a number between 1 and 7.
5. If the input is not an integer, an error message will prompt you to enter a valid integer.

## Example Output

### Valid Input
Enter a number between 1 and 7: 3
Wednesday


### Out-of-Range Input

Enter a number between 1 and 7: 10
Error: Please enter a number between 1 and 7.

### Non-Integer Input

Enter a number between 1 and 7: hello
Error: Invalid input. Please enter an integer.

Requirements
Python 3.10+ (for match-case syntax)
License
This project is open source and available under the MIT License.
