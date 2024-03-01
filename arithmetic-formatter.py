def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_arithmetically = ""
    first_number = ""
    second_number = ""
    line_of_dashes = ""
    resul = ""

    for problem in problems:
        # Split the problem numbers and operator
        number1, sign, number2 = problem.split()

        # Validate the numbers and operator
        if not (number1.isdigit() and number2.isdigit()):
            return "Error: Numbers must only contain digits."
        if sign not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers are more than four digits
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Convert numbers to integers
        number1 = int(number1)
        number2 = int(number2)

        # Determine the maximum length of numbers
        max_length = max(len(str(number1)), len(str(number2)))

        # Build the top line
        first_number += str(number1).rjust(max_length + 2) + '    '

        # Build the bottom line with number2 and sign
        second_number += sign + ' ' + str(number2).rjust(max_length) + '    '

        # Build the dashes line
        line_of_dashes += '-' * (max_length + 2) + '    '

        # Calculate answers if needed
        if show_answers:
            if sign == '+':
                answer = number1 + number2
            else:
                answer = number1 - number2
            resul += str(answer).rjust(max_length + 2) + '    '

    # Combine all lines
    arranged_arithmetically = first_number.rstrip() + '\n' + second_number.rstrip() + '\n' + line_of_dashes.rstrip()

    # Add answers if needed
    if show_answers:
        arranged_arithmetically += '\n' + resul.rstrip()

    return arranged_arithmetically


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')